#!/bin/python3

import os


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = list(a)
    b = list(b)
    a.sort()
    b.sort()
    result = []
    while len(a) > 0:
        if len(b) > 0:
            if a[0] == b[0]:
                a.pop(0)
                b.pop(0)
            elif ord(a[0]) < ord(b[0]):
                result.append(a.pop(0))
            else:
                result.append(b.pop(0))
        else:
            while len(a) > 0:
                result.append(a.pop(0))
            break
    while len(b) > 0:
        result.append(b.pop(0))
    res = len(result)
    print(res)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = input()
    b = input()
    res = makeAnagram(a, b)
    fptr.write(str(res) + '\n')
    fptr.close()
