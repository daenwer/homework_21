#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    s = s[::-1]
    start = 0
    step = 1
    res = 0
    # print('s = {}'.format(s))
    # print('len(s) = {}'.format(len(s)))
    for step in range(1, len(s)):
        # print('step = {}'.format(step))
        for start in range(0, len(s) - step):
            # print('start = {}'.format(start))
            key = list(s[start:(start + step)])
            key.sort()
            # print('key = {}'.format(key))
            for i in range((start + 1), ((len(s) - step) + 1)):
                # print('key = {}, s[i:(i+step)] = {}'.format(key, s[i:(i+step)]))
                answer = list(s[i:(i + step)])
                answer.sort()
                if key == answer:
                    # print('key = {}, s[i:(i+step)] = {}'.format(key, s[i:(i+step)]))
                    res += 1
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
