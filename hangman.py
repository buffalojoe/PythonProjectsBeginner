import random
import sys

# Finds a random word from a dictionary of words
def findWord(dictionary):
    words = []
    inputFile = open(dictionary, "r")
    
    for line in inputFile.readlines():
        line = line.strip()
        words.append(line)

    index = random.randint(0, len(words) - 1)
    while len(words[index]) < 5:
        index = random.randint(0, len(words) - 1)

    foundWord = [" "] * len(words[index])
    
    return (words[index], foundWord)

# Select a mode that will determine the number of guesses allowed
def modeSelect(word):
    mode = input("Select a difficulty:\nEasy(e)\nMedium(m)\nHard(h)\n").lower()

    if mode == "easy" or mode == "e":
        guessLimit = len(word) + 12
        mode = "easy"
    elif mode == "medium" or mode == "m":
        guessLimit = len(word) + 6
        mode = "medium"
    elif mode == "hard" or mode == "h":
        guessLimit = len(word) + 1
        mode = "hard"
    else:
        print("Invalid mode selection")
        sys.exit()
    
    return (guessLimit, mode)

# Log results of a game of hangman
def logResult(word, mode, guessCount, guessLimit, result):
    file = open("hangmanResults.txt", "a")
    resultMap = {"Word" : word, "Mode" : mode, "Guess Count" : guessCount, "Guess Limit" : guessLimit, "Result": result}
    result = ""
    for key in resultMap.keys():
        result += key + " : " + str(resultMap[key]) + ", "
    
    result = result[:-2]
    file.write(result + "\n")
    file.close()
    return None

# Play the hangman game
def guess(word, foundWord, guessCount, guessLimit, guessedLetters):
    print(f"Word progress: {foundWord}")
    print(f"Guessed Letters: {guessedLetters}")
    print(f"Guess Count: {guessCount}\n")

    if guessCount == guessLimit:
        print(f"All out of guesses. You lose! The word was {word}")
        return ("Lost", guessCount)
    
    if "".join(foundWord) == word:
        print("You got it! You Win!")
        return ("Won", guessCount)
    
    userGuess = input("Guess a letter: ")

    if not userGuess.isalpha():
        print("Letters only!")
        return guess(word, foundWord, guessCount, guessLimit, guessedLetters)

    if len(userGuess) == 1:
        if userGuess in guessedLetters:
            print("You already guessed that letter!")
            return guess(word, foundWord, guessCount, guessLimit, guessedLetters)
        else:
            guessedLetters.append(userGuess)
    
    guessCount += 1
    if userGuess == word:
        print("You got it! You Win!")
        return ("Won", guessCount)

    for i in range(len(word)):
        if userGuess == word[i]:
            foundWord[i] = userGuess

    return guess(word, foundWord, guessCount, guessLimit, guessedLetters)

# Run the program
def main():
    dictionary = "dictionary.txt"
    word, foundWord = findWord(dictionary)

    guessLimit, mode = modeSelect(word)

    guessCount = 0
    guessedLetters = []

    print("INSTRUCTIONS:")
    print("Guess a letter or the word on each turn")
    print(f"Each guess adds to your guess count. You only get {guessLimit} guesses!")
    print(f"Your word is {len(word)} letters long\n")

    result, guessCount = guess(word, foundWord, guessCount, guessLimit, guessedLetters)
    logResult(word, mode, guessCount, guessLimit, result)

main()