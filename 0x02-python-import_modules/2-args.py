#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    i = len(argv) - 1
    if i == 0:
        print("{:d} arguments.".format(i))
    elif i == 1:
        print("{:d} argument:".format(i))
    else:
        print("{:d} arguments:".format(i))
    if i >= 1:
        for position in range(0, i):
            print("{:d}: {}".format(position + 1, argv[position + 1]))
