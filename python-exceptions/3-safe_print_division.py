#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a // b
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(float(result) if result else result))
    return float(result) if result is not None else result


def main():
    a = 12
    b = 2
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

    a = 12
    b = 0
    result = safe_print_division(a, b)
    print("{:d} / {:d} = {}".format(a, b, result))

main()
