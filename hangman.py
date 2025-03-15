import random

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
    
    return words[index]

def modeSelect(word):
    mode = input("Select a difficulty:\nEasy\nMedium\nHard\n").lower()

    if mode == "easy" or mode == "e":
        guessLimit = len(word) + 15
    elif mode == "medium" or mode == "m":
        guessLimit = len(word) + 8
    elif mode == "hard" or mode == "h":
        guessLimit = len(word) + 1
    else:
        print("Invalid mode selection")
        return None
    
    return guessLimit

# Play the hangman game
def guess(word, foundWord, guessCount, guessLimit, guessedLetters):
    print(f"Word progress: {foundWord}")
    print(f"Guess Count: {guessCount}\n")

    if guessCount == guessLimit:
        print(f"All out of guesses. You lose! The word was {word}")
        return None
    
    if "".join(foundWord) == word:
        print("You got it! You Win!")
        return None
    
    userGuess = input("Guess a letter: ")

    if not userGuess.isalpha():
        print("Letters only!")
        guess(word, foundWord, guessCount, guessLimit, guessedLetters)
        return None

    if len(userGuess) == 1:
        if userGuess in guessedLetters:
            print("You already guessed that letter!")
            guess(word, foundWord, guessCount, guessLimit, guessedLetters)
            return None
        else:
            guessedLetters.append(userGuess)
    
    guessCount += 1
    if userGuess == word:
        print("You got it!")
        return None 

    for i in range(len(word)):
        if userGuess == word[i]:
            foundWord[i] = userGuess

    guess(word, foundWord, guessCount, guessLimit, guessedLetters)

# Run the program
def main():
    dictionary = "dictionary.txt"
    word = findWord(dictionary)

    guessLimit = modeSelect(word)
    if guessLimit == None:
        return None

    guessCount = 0
    guessedLetters = []
    foundWord = []

    for i in range(len(word)):
        foundWord.append(" ")

    print("INSTRUCTIONS:")
    print("Guess a letter or the word on each turn")
    print(f"Each guess adds to your guess count. You only get {guessLimit} guesses!")
    print(f"Your word is {len(word)} letters long\n")

    guess(word, foundWord, guessCount, guessLimit, guessedLetters)

main()