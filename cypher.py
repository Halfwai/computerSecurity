import math

def encrypt(firstKey, secondKey, phrase):
    offset = ord("a")
    limit = ord("z")
    encryptedPhrase = []
    for i in range(0, len(phrase)):
        shift = ord(firstKey[i % len(firstKey)]) - offset
        newChar = ord(phrase[i]) + shift
        if newChar > limit:
            newChar -= 26
        encryptedPhrase.append(chr(newChar))
    grid = []
    for i in range(len(secondKey)):
        index = i
        row = []
        while index <= len(encryptedPhrase) - 1:
            row.append(encryptedPhrase[index])
            index += len(secondKey)
        grid.append(row)
    alphabet = "abcdefghijklmnopqrstuvwqyz"
    encryptedPhrase = []
    for i in range(len(alphabet)):
        for j in range(len(secondKey)):
            if alphabet[i] == secondKey[j]:
                for letter in grid[j]:
                    encryptedPhrase.append(letter)
    return "".join(encryptedPhrase)

def deCrypt(firstKey, secondKey, phrase):
    alphabet = "abcdefghijklmnopqrstuvwqyz"
    grid = []
    for i in range(len(secondKey)):
        grid.append([])
    phraseIndex = 0
    for i in range(len(alphabet)):
        for j in range(len(secondKey)):
            if alphabet[i] == secondKey[j]:
                inputNumber = math.floor(len(phrase)/len(secondKey))
                if len(phrase) % len(secondKey) > j:
                    inputNumber += 1
                for k in range(phraseIndex, phraseIndex + inputNumber):
                    grid[j].append(phrase[k])
                phraseIndex += inputNumber
    partlyUnencryptedPhrase = []
    for i in range(len(phrase)):
        partlyUnencryptedPhrase.append(grid[i % len(secondKey)][math.floor(i/len(secondKey))])
    offset = ord("a")
    unencryptedPhrase = []
    for i in range(0, len(partlyUnencryptedPhrase)):
        shift = ord(firstKey[i % len(firstKey)]) - offset
        newChar = ord(partlyUnencryptedPhrase[i]) - shift
        if newChar < offset:
            newChar += 26
        unencryptedPhrase.append(chr(newChar))
    return ''.join(unencryptedPhrase)

def deTransposition(key, phrase):
    alphabet = "abcdefghijklmnopqrstuvwqyz"
    grid = []
    for i in range(len(key)):
        grid.append([])
    phraseIndex = 0
    for i in range(len(alphabet)):
        for j in range(len(key)):
            if alphabet[i] == key[j]:
                inputNumber = math.floor(len(phrase)/len(key))
                if len(phrase) % len(key) > j:
                    inputNumber += 1
                for k in range(phraseIndex, phraseIndex + inputNumber):
                    grid[j].append(phrase[k])
                phraseIndex += inputNumber
    unencryptedPhrase = []
    for i in range(len(phrase)):
        unencryptedPhrase.append(grid[i % len(key)][math.floor(i/len(key))])
    return "".join(unencryptedPhrase)

def deVigenere(key, phrase):
    offset = ord("a")
    unencryptedPhrase = []
    for i in range(0, len(phrase)):
        shift = ord(key[i % len(key)]) - offset
        newChar = ord(phrase[i]) - shift
        if newChar < offset:
            newChar += 26
        unencryptedPhrase.append(chr(newChar))
    return ''.join(unencryptedPhrase)


phrase = "countless path one destination"

vigKey = "secretkey"

transKey = "secondkey"

phrase = phrase.replace(" ", "")

print(phrase)

encryptedPhrase = (encrypt(vigKey, transKey, phrase))

print(encryptedPhrase)

deCryptedPhrase = deCrypt(vigKey, transKey, encryptedPhrase)

print(deCryptedPhrase)


