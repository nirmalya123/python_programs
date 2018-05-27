"""
https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem
"""
class MyQueue(object):    
    def __init__(self):
        self.push_stk = []
        self.pop_stk = []
    
    def fill_empty_stk(self):
        while self.push_stk:
            self.pop_stk.append(self.push_stk.pop())
    
    def peek(self):
        if len(self.pop_stk) == 0:
            self.fill_empty_stk()
        return self.pop_stk[-1]
        
    def pop(self):
        if len(self.pop_stk) == 0:
            self.fill_empty_stk()
        self.pop_stk.pop()
        
    def put(self, value):
        self.push_stk.append(value)
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
        