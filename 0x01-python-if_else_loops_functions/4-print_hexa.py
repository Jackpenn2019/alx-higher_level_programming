#!/usr/bin/python3
# Author - Isaiah Kibet
def print_hexa():
    """Print numbers from 0 to 98 in decimal and hexadecimal"""
    for i in range(0, 99):
        print("{} =".format(i), hex(i))


print_hexa()
