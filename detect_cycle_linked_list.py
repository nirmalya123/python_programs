"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
https://www.hackerrank.com/challenges/ctci-linked-list-cycle/problem
"""


def has_cycle(head):
    if head == None or head.next == None:
        #print("empty list")
        return False
    cur = head.next
    prev = head
    while cur.next != None and cur != prev:
        cur = cur.next
        prev = prev.next
        cur = cur.next
    if cur.next == None: # List traversed till the tail
        #print("full travered")
        return False
    return True
