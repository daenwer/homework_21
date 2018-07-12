#!/bin/python3

import math
import os
import random
import re
import sys

# 4
# add hack
# add hackerrank
# find hac
# find hak

if __name__ == '__main__':
    n = int(input())

    data_name = {}


    def letters_app(counter, current_dict):
        """
        Записываем буквы имен в словарь
        """
        if contact[counter] in current_dict:
            current_dict[contact[counter]]['amount'] += 1
        else:
            current_dict[contact[counter]] = {'amount': 1}
        current_dict = current_dict[contact[counter]]
        counter += 1
        if counter < stop:
            letters_app(counter, current_dict)
        return


    for n_itr in range(n):
        opContact = input().split()
        op = opContact[0]
        contact = opContact[1]
        if op == 'add':
            stop = len(contact)
            current_dict = data_name
            counter = 0
            letters_app(counter, current_dict)

        else:
            current_dict = data_name
            for letter in contact:
                if letter in current_dict:
                    result = current_dict[letter]['amount']
                    current_dict = current_dict[letter]
                else:
                    result = 0
                    break
            print(result)
