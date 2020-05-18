#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    try:
        for items in my_list[0:x]:
            print("{}".format(items), end="")
            i += 1
    except IndexError:
        print("INVALID INDEX")
    finally:
        print()
        return (i)
