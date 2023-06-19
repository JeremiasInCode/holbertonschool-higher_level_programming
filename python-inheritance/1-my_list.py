#!/usr/bin/python3
""" Task 1 """


class MyList(list):
    """ Prints the list, but sorted in ascending sort """
    def print_sorted(self):
        print(sorted(self))
def main():
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
main()