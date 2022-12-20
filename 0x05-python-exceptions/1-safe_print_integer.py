#!/usr/bin/python3

def safe_print_integer(value):
    # initializing the flag to 'True'
    flag = True
    
    # try to convert value to integer
    try:
        value = int(value)
    
    # catch the exception
    except ValueError:
        flag = False

    # Else print the value
    else:
        print("{:d}".format(value))
    
    # Finally always return the flag
    finally:
        return (flag)
