import random

def userInputs():
    acceptedInput = ['y', 'yes', 'n', 'no']
    
    length = ""

    while length.isdigit() == False:
        length = input("Password length: ")
    
    length = int(length)

    includeCapitals = None

    while includeCapitals not in acceptedInput:
        includeCapitals = input("Include capitals (Y/N)? ").lower()
    
    if includeCapitals == 'y' or includeCapitals == 'yes':
        includeCapitals = True
    else:
        includeCapitals = False

    includeNumbers = None

    while includeNumbers not in acceptedInput:
        includeNumbers = input("Include numbers (Y/N)? ").lower()
    
    if includeNumbers == 'y' or includeNumbers == 'yes':
        includeNumbers = True
    else:
        includeNumbers = False

    includeSymbols = None

    while includeSymbols not in acceptedInput:
        includeSymbols = input("Include symbols (Y/N)? ").lower()
    
    if includeSymbols == 'y' or includeNumbers == 'yes':
        includeSymbols = True
    else:
        includeSymbols = False
    
    return (length, includeCapitals, includeNumbers, includeSymbols)

def generatePassword(length, includeCapitals, includeNumbers, includeSymbols):
    validUnicode = []
    password = ""

    for i in range(97, 123):
        validUnicode.append(i)

    if includeCapitals:
        for i in range(65, 90):
            validUnicode.append(i)
    
    if includeNumbers:
        for i in range(48, 58):
            validUnicode.append(i)

    if includeSymbols:
        for i in range(33, 48):
            validUnicode.append(i)
        
        for i in range(58, 64):
            validUnicode.append(i)
        
        for i in range(91, 97):
            validUnicode.append(i)
        
        for i in range(123, 127):
            validUnicode.append(i)

    for i in range(1, length + 1):
        ordValue = validUnicode[random.randint(0, len(validUnicode) - 1)]
        password += chr(ordValue)

    return password

def main():
    length, includeCapitals, includeNumbers, includeSymbols = userInputs()
    password = generatePassword(length, includeCapitals, includeNumbers, includeSymbols)
    print(password)

main()