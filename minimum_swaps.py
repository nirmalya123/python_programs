"""
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=arrays

An unordered array of consecutive integers {1,...N} is given.
Count the minimum numbers of swaps needed to sort the array in ascending order.
Sample Input
5
2 3 4 1 5
Sample Output
3
"""
import os

def minimumSwaps(arr):
    count = 0
    i = 0
    n = len(arr)
    while i < n:
        if arr[i] == i + 1:
            i = i + 1
        else:
            temp = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = temp
            count = count + 1            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()