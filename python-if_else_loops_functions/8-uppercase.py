#!/usr/bin/python3
def uppercase(str):
    for element in range(len(str)):
        elementN = ord(str[element])
        if (elementN >= 97 and elementN <= 122):
            elementN = elementN - 32
        print("{}".format(chr(elementN)), end="")
    print("")
