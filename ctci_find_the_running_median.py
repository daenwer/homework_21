#!/bin/python3


if __name__ == '__main__':
    n = int(input())

    left_list = []
    middle_list = []
    right_list = []


    def number(result):
        """
        Форматирует результат в соответствии с заданием
        """
        res = int(result * 10) / 10
        return res


    def record():
        """
        Записывае значения из middle_list в кучи
        значение большее в right_list
        значение большее в left_list
        """
        right_list.insert(0, middle_list.pop())
        left_list.append(middle_list.pop())


    def sorted():
        """
        Сортирует среднюю кучу слева на право
        слева наименьшее значение справа наибольшее
        """
        if middle_list[1] < middle_list[0]:
            middle_list[1], middle_list[0] = middle_list[0], middle_list[1]
        return


    def sorting(stack, num, start, stop):
        """
        Сортирует кучу слева на право
        слева наименьшее значение справа наибольшее
        """
        if start > stop:
            stack.insert(start, num)
        else:
            mid = (start + stop) // 2
            if num == stack[mid]:
                stack.insert(mid, num)
            elif num < stack[mid]:
                return sorting(stack, num, start, mid - 1)
            else:
                return sorting(stack, num, mid + 1, stop)


    flag = 1
    for _ in range(n):
        num = int(input())
        if flag == 1:
            """
            пришло первое число в middle_list.append, кучи пока пустые
            (left_list и right_list пустые)
            """
            middle_list.append(num)
            result = number(num)
            flag = 2

        elif flag == 2:
            """
            пришло второе число в middle_list.append, кучи пока пустые
            (left_list и right_list пустые)
            """
            middle_list.append(num)
            result = number((middle_list[0] + middle_list[1]) / 2)
            flag = 0
            sorted()
            record()

        else:
            if num <= left_list[-1]:
                sorting(left_list, num, 0, (len(left_list) - 1))
                middle_list.append(left_list.pop())
            else:
                sorting(right_list, num, 0, (len(right_list) - 1))
                middle_list.append(right_list.pop(0))
            if len(middle_list) == 1:
                result = number(middle_list[0])
            elif len(middle_list) == 2:
                sorted()
                result = number((middle_list[0] + middle_list[1]) / 2)
                record()

        print(result)
