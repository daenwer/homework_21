#!/bin/python3

import os


# Complete the countInversions function below.
def sort_array(arr_left, arr_right, counter):
    array_mid = []
    while len(arr_left) > 0 and len(arr_right) > 0:
        if arr_left[0] <= arr_right[0]:
            number = arr_left.pop(0)
            array_mid.append(number)
        else:
            number = arr_right.pop(0)
            array_mid.append(number)
            counter += len(arr_left)
    if len(arr_left) > 0:
        while len(arr_left) > 0:
            number = arr_left.pop(0)
            array_mid.append(number)
    else:
        while len(arr_right) > 0:
            number = arr_right.pop(0)
            array_mid.append(number)
    return counter, array_mid


def countInversions(arr_res, counter):
    if len(arr_res) > 1:
        mid = len(arr_res) // 2
        arr_left = arr_res[:mid]
        arr_right = arr_res[mid:]
        if len(arr_left) > 1:
            counter, arr_left = countInversions(arr_left, counter)
        if len(arr_right) > 1:
            counter, arr_right = countInversions(arr_right, counter)
        counter, arr_mid_res = sort_array(arr_left, arr_right, counter)
        return counter, arr_mid_res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))
        counter = 0
        result, counter = countInversions(arr, counter)
        fptr.write(str(result) + '\n')
        print(counter)
    fptr.close()
