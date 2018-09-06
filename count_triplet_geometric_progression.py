"""
Function should return the number of triplets forming a geometric progression for a given r  as an integer.

https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
from collections import Counter
# Complete the countTriplets function below.
def countTriplets(arr, r):
    r2 = Counter()
    r3 = Counter()
    count = 0
    
    for i in range(len(arr)):
        if arr[i] in r3:
            count = count + r3[arr[i]]
        
        if arr[i] in r2:
            r3[arr[i]*r] += r2[arr[i]] # For the middle one update its occurance for the right side
        
        r2[arr[i]*r] += 1 # Add for each occurrance of the left side

    return count
