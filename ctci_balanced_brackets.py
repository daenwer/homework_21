#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    t = int(input())

    accord = {'{': '}', '[': ']', '(': ')'}
    for t_itr in range(t):
        expression = input()
        symbols = list(expression)
        stack = [symbols[0]]
        symbols.pop(0)
        for symbol in symbols:
            if len(stack) == 0:
                stack.append(symbol)
            elif stack[-1] in accord:
                if accord[stack[-1]] == symbol:
                    stack.pop()
                else:
                    stack.append(symbol)
            else:
                stack.append(symbol)
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')
