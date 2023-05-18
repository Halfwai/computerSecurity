def vigenere(key, phrase):
    offset = ord("a")
    limit = ord("z")
    cypher = []
    for i in range(0, len(phrase) - 1):
        shift = ord(key[i % len(key)]) - offset
        newChar = ord(phrase[i]) + shift
        if newChar > limit:
            newChar -= 26
        cypher.append(chr(newChar))
    return ''.join(cypher)

def transposition(key, phrase):
    grid = []
    for i in range(len(key)):
        index = i
        row = []
        while index <= len(phrase) - 1:
            row.append(phrase[index])
            index += len(key)
        grid.append(row)
    newKey = list(key)
    newKey.sort()
    print(newKey)


phrase = "countless path one destination"

phrase = phrase.replace(" ", "")

vigKey = "secretkey"

phrase = (vigenere(vigKey, phrase))

transKey = "secondkey"

transposition(transKey, phrase)




