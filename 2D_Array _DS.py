#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):  # print(arr)
    res = []
    for j in range(4):
        for i in range(4):
            res_prom = arr[j][i] + arr[j][i + 1] + arr[j][i + 2] + arr[j + 1][
                i + 1] + arr[j + 2][i] + arr[j + 2][i + 1] + arr[j + 2][i + 2]
            res.append(res_prom)
    max_res = max(res)
    return max_res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
