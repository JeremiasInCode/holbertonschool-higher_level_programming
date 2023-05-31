#!/usr/bin/python3
def fizzbuzz():
    for element in range(1, 101):
        if element % 3 == 0 and element % 5 == 0:
            print("FizzBuzz", end=" ")
        elif element % 3 == 0:
            print("Fizz", end=" ")
        elif element % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(element, end=" ")
