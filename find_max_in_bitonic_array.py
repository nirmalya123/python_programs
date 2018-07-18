# Find the index of the max value in a Bitonic array
# Bitonic array is an array where the sequence first increases then decreases

arr1 = [99,100,102,103,104,55,50,40,20,10,6]
arr2 = [99,100,102,103,104,105]
arr3 = [55,50,40,20,10,6]
arr4 = [99,100,102,103,104,105,50]
arr5 = [110,55,50,40,20,10,6]

def find_max_bitonic(arr,lb, ub):
    #print([arr[x] for x in range(lb,ub)])
    if lb == ub:
        return lb
    mid = (lb + ub)//2
    if arr[mid] > arr[mid + 1]:
        if arr[mid] > arr[mid - 1]:
            return mid
        else:
            return find_max_bitonic(arr,lb,mid - 1)
    else:
        #arr[mid] <= arr[mid + 1]:
        return find_max_bitonic(arr,mid + 1, ub)
print("-----------------------------------")
print(arr1[find_max_bitonic(arr1,0,len(arr1) - 1)])
print("-----------------------------------")
print(arr2[find_max_bitonic(arr2,0,len(arr2) - 1)])
print("-----------------------------------")
print(arr3[find_max_bitonic(arr3,0,len(arr3) - 1)])
print("-----------------------------------")
print(arr4[find_max_bitonic(arr4,0,len(arr4) - 1)])
print("-----------------------------------")
print(arr5[find_max_bitonic(arr5,0,len(arr5) - 1)])
print("-----------------------------------")