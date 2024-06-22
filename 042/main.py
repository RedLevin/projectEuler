def wordValue(word, characters):
    value = 0
    for c in word:
        value += characters[c]
    return value

def triangleNumbers(n):
    triangleNumberList = []
    number = 0
    for i in range(1, n):
        number += i
        triangleNumberList.append(number)
    return triangleNumberList

def isTriangleNumber(n, triangleNumbersList):
    return n in triangleNumbersList

file = open("0042_words.txt", "r")

words = (file.readlines()[0]).replace('"', '').split(",")

characters = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

triangleNumbersList = triangleNumbers(100)

count = 0

for word in words:
    if(isTriangleNumber(wordValue(word, characters), triangleNumbersList)): count += 1

print(count)