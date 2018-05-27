"""
https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
"""
top = -1
stk = []
opening = {'(':0,'{':1,'[':2}
closing = {')':0,'}':1,']':2}

def push_stk(t):
    global top
    global stk
    stk.append(t)
    #print("push ",t,top,stk)
    top += 1
    
def pop_stk():
    global top
    global stk
    t = stk.pop()
    #print("pop ",t,top,stk)
    top -= 1
    
def is_matched(expression):
    global stk
    global top
    stk = []
    top = -1
    if len(expression) < 2:## or expression[0] in closing:
        return False
    
    for t in expression:
        if t in opening:
            push_stk(t)
        elif t in closing: 
            if top <= -1:
                return False
            if opening[stk[top]] == closing[t]:
                pop_stk()
            else:
                return False
    if top <= -1:
        return True
    else:
        return False
        

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
