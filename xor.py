import math

def getAscii(letter):
    return ord(letter)

def asciiToLetter(number):
    return chr(number)

def decimalToBinary(num):
    binaryNum = []
    while num != 0:
        testNum = str(num % 2)
        binaryNum.insert(0, testNum)
        num = math.floor(num / 2)
    while len(binaryNum) != 8:
        binaryNum.insert(0, "0")
    return ''.join(binaryNum)

def convertLetterToBinary(letter):
    letter = getAscii(letter)
    letter = decimalToBinary(letter)
    return letter

def compare(num1, num2):
    xor = []
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            xor.append("1")
        else:
            xor.append("0")
    return ''.join(xor)

def binaryToDecimal(binaryNum):
    decimalNumber = 0
    factor = 1
    for i in range(len(binaryNum) - 1, 0, -1):
        decimalNumber += int(binaryNum[i]) * factor
        factor *= 2
    return decimalNumber

def stringToXor(string, key):
    output = []
    keyBinary = decimalToBinary(key)
    for letter in string:
        letterBinary = decimalToBinary(getAscii(letter))
        xor = compare(keyBinary, letterBinary)
        decimalXor = binaryToDecimal(xor)
        output.append(decimalXor)
    return output

# code = [92,113,120,120,123,52,67,123,102,120,112,53] 
# print(code)
# key = decimalToBinary(53)
# translatedWord = []
# for number in code:
#     bin = decimalToBinary(number)
#     xor = compare(key, bin)
#     decimal = binaryToDecimal(xor)
#     letter = asciiToLetter(decimal)
#     translatedWord.append(letter)
# print(''.join(translatedWord))

for i in range(255):
    print(i)