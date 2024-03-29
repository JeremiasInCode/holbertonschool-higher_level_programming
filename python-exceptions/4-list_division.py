#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for element in range(list_length):
        list.append(0)
        try:
            list[element] = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            pass
    return (list)
