#!/usr/bin/python3
# Author - Kibet
for x in range(10):
    for y in range(10):
        if x == 8 and y == 9:
            print("{}{}".format(x, y))
        else:
            if "{}{}".format(x, y) < "{}{}".format(y, x):
                print("{}{}".format(x, y), end=", ")
