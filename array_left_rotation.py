'''
A left rotation operation on an array shifts each of the array's elements one unit to the left. 

Given an array a of n integers and a number,d , perform d left rotations on the array. Then print the updated array as a single line of space-separated integers.

Sample Input
5 4
1 2 3 4 5

Sample Output
5 1 2 3 4
https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
'''
def array_left_rotation(a, n, k):
    arr2 = []
    arr2.extend(x for x in a[k:])
    arr2.extend(x for x in a[:k])
    return arr2
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(answer, sep=' ')
