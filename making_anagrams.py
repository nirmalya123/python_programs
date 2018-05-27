'''
We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.
https://www.hackerrank.com/challenges/ctci-making-anagrams/problem
'''


from collections import Counter
def number_needed(a,b):
    count_a = Counter()
    count_b = Counter()
    for x in list(a):
        count_a[x] += 1 
    for y in list(b):
        count_b[y] += 1
    count = 0
    for k,v in count_a.most_common():
        if count_b[k] == 0:
            count += v
        else:
            count += abs(v - count_b[k])
    for k,v in count_b.most_common():
        if count_a[k] == 0:
            count += v
    return count

a = input().strip()
b = input().strip()

print(number_needed(a, b))