"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem
"""
""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    in_order_list = []
    in_order_stk = []
    node1 = root
    while node1 or len(in_order_stk) > 0:
        if node1:
            in_order_stk.append(node1)
            node1 = node1.left
        else:
            node1 = in_order_stk.pop()
            in_order_list.append(node1.data)
            node1 = node1.right    

    l = len(in_order_list) - 1

    if l <= 0:
        return False
    while l > 0:
        if in_order_list[l] <= in_order_list[l-1]:
            return False
        l -= 1
    return True