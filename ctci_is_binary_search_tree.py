""" Node is defined as
"""


class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


d = Node(data=5)
e = Node(data=15)
f = Node(data=25)
i = Node(data=35)
b = Node(data=10, left=d, right=e)
c = Node(data=30, left=f, right=i)
a = Node(data=20, left=b, right=c)


def checkBST(root):
    result = []

    def recursion(root):
        if root.left:
            recursion(root.left)
        result.append(root.data)

        if root.right:
            recursion(root.right)
        return result

    recursion(root)

    result_sort = []
    for i in result:
        result_sort.append(i)
    result_sort.sort()
    if result == result_sort and len(result) == len(set(result)):
        return True
    else:
        return False


print(checkBST(a))

