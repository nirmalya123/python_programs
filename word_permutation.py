'''
A person found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
https://www.hackerrank.com/challenges/ctci-ransom-note/problem
'''
from collections import Counter 
def ransom_note(magazine, ransom):
    if len(ransom) > len(magazine):
        return False
    count_m = Counter()
    count_r = Counter()
    for x in magazine:
        count_m[x] += 1
    for x in ransom:
        count_r[x] += 1
    flag = True
    for x,v in count_r.most_common():
        if count_r[x] > count_m[x]:
            flag = False
    return flag

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    