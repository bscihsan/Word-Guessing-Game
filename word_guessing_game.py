import sys
import time

#	https://github.com/bscihsan

if len(sys.argv) != 3:  # Exiting from program if wanted terminal condition did not satisfied.
    print("You must write two arguments for this program")
    exit(-1)

correctWords = open(sys.argv[1],  "r", encoding="utf-8-sig")  # Following lines are for making file read, operated, appended to dictionary and closing it at the end.
readCorrectWords = correctWords.readlines()
dictCorrectWords = {line.strip().replace("I", "ı").replace("İ", "i").lower().split(":")[0]: line.strip().replace("I", "ı").replace("İ", "i").lower().split(":")[1].split(",") for line in readCorrectWords}
correctWords.close()
letterValues = open(sys.argv[2], "r", encoding="utf-8-sig")
readLetterValues = letterValues.readlines()
dictLetterValues = {line.strip().replace("I", "ı").replace("İ", "i").lower().split(":")[0]: line.strip().replace("I", "ı").replace("İ", "i").lower().split(":")[1] for line in readLetterValues}
letterValues.close()
for line in dictCorrectWords.keys():  # This code loops the lines at correct words for making game playable.
    guessedOnes = []  # Holding guessed ones for checking if user guessed that word before, also it used for exiting from the loop.
    beginning = time.time()  # Holding beginning time for checking if user still have time.
    flag = True  # Creating a flag that controlled for every loop.
    point = 0  # The variable that holds point of the player.
    print("Shuffled letters are:\t%s\tPlease guess words for these letters with minimum three letters" % line)  # Printing mixed letters to user.
    while flag:
        guess = input("Guessed Word: ").strip().replace("I", "ı").replace("İ", "i").lower()  # Taking a guess from user and checking if it is available and also guessed before, and doing necessary operations.
        if guess in dictCorrectWords[line]:
            if not (guess in guessedOnes):
                guessedOnes.append(guess)
                tempPoint = 0  # This part of code evaluates score of the user for his/her guess.
                for letter in guess:
                    tempPoint += int(dictLetterValues[letter])
                point += len(guess) * tempPoint
            else:
                print("This word is guessed before")
        else:
            print("your guessed word is not a valid word")
        timeLeft = int(30 - time.time() + beginning)
        print("You have %d time" % timeLeft)
        if not(timeLeft > 0 and len(guessedOnes) < len(dictCorrectWords[line])):  # Forcing the loop exit and printing score of the player if time is over or player has been guessed all the words available for given letters.
            flag = False
            print("Score for %s is %d and" % (line, point), end=" ")
            if len(guessedOnes) > 0:
                print("guessed words are", end=": ")
                for word in guessedOnes[0:-1]:
                    print("%s" % word, end="-")
                print(guessedOnes[-1])
            else:
                print("no word were guessed correctly.")
