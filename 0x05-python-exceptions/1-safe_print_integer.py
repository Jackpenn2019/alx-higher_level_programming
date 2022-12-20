#!/usr/bin/python3

def safe_print_integer(value):
    flag = True
    
    try:
        value = int(value)
    
    except (TypeError, ValueError):
        flag = False

    else:
        print("{:d}".format(value))
    
    finally:
        return (flag)
