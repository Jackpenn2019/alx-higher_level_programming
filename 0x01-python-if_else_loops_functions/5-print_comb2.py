#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(100):
        if i == 99:
            print("{}".format(i))
        else:
            print("{:02}".format(i), end=", ")
