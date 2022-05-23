

#NOTE: Binary Search only works if the array has already been sorted

#PseudoCode
"""
1. define max and min for array
2. ensure function only runs as long as min is at least equal to the max
3. if target is equal to mid, then return mid
4. if target is less than mid, discard upper half, set max to mid-1
5. if target is more than mid, discard lower hald, set min to mid+1
6. Repeat 3-5 until either value is found or run out of space
7. Return index of -1 if target not found
"""

def binary_search (arr, target):
    (min, max) = (0, len(arr) -1)

    while min <= max:

        mid = (min + max) // 2
        if target == arr[mid]:
            return mid

        elif target <= arr[mid]:
            max = mid-1
        
        else:
            min = mid+1
        
    return -1



#create array of numbers
nums = [2, 3, 5, 7, 8, 10, 12, 15, 18, 20]
target = 98
index = binary_search(nums, target)

if index != -1:
    print('Element {} found at index {}'.format(target, index))
else:
    print("Element {} not found in array".format(target))




