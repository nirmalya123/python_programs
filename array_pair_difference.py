"""
You will be given an array of integers and a target value. 
Determine the number of pairs of array elements that have a difference equal to a target value.
https://www.hackerrank.com/challenges/pairs/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search
"""
def pairs(k, arr):
    i=0
    j=1
    count=0
    nums = sorted(arr)
    #print(nums)
    
    while(j < n):
        diff = nums[j] - nums[i]
        
        if (diff == k):
            count = count + 1
            j = j + 1
        elif (diff > k):
            i = i + 1
        elif (diff < k):
            j = j + 1
    return count
