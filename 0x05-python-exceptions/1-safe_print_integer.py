#!/usr/bin/python3

def safe_print_integer(value):
    flag = True
    
    try:
        value = int(value)
    
    except ValueError:
        flag = False

    else:
        print("{:d}".format(value))
        print("")
    
    finally:
        return (flag)
