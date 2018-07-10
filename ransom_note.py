#!/usr/bin/python3
# -*- coding: utf-8 -*-


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    note_sum = {}
    for work in note:
        if work in note_sum:
            note_sum[work] += 1
        else:
            note_sum[work] = 1
    magazine_sum = {}
    for work in magazine:
        if work in magazine_sum:
            magazine_sum[work] += 1
        else:
            magazine_sum[work] = 1
    flag = True
    for work in note_sum:
        if work not in magazine_sum:
            flag = False
            break
        elif note_sum[work] > magazine_sum[work]:
            flag = False
            break
    if flag is True:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    magazine = input().rstrip().split()
    note = input().rstrip().split()
    checkMagazine(magazine, note)
