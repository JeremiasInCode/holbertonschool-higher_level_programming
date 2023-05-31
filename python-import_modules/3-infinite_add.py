#!/usr/bin/python3
import sys
if __name__ == "__main__":
    # Excluimos el primer elemento de la lista (args).
    args = sys.argv[1:]
    list = []
    add = 0
    for first_element in args:
        try:
            first_element = int(first_element)
            list.append(first_element)
        except ValueError:
            print("Error")

    for second_element in list:
        add += second_element

    print(add)
