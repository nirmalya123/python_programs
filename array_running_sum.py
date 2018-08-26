"""
https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
Sample oprations
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]

Sample Input
5 3
1 2 100
2 5 100
3 4 100
Sample Output
200
"""
import os
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)
    for q in queries:
        arr[q[0] - 1] += q[2]   ## Add the needed value as the left most cell. 
                                ## For traling cell within the range it will be added in the next for loop
        arr[q[1]] -= q[2]       ## As a precaution for the running sum subtract the sum from the cell succeding the right most limit.

    for i in range(1, len(arr)):
        arr[i] += arr[i-1]      ## Find the running sum. All overlapping will be taken care of here.

    return max(arr)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()