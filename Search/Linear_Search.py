#create array to search
nums = [1,5,0,8,3,7]

for i in range(len(nums)):
   if nums[i] == 0:
        print("Found number 0 at index {}".format(i))
        exit


#implemented in a function
def linear_search(arr, num):
    upper = len(arr)
    for i in range(upper):
        if arr[i] == num:
            print("Found number {} at index {}".format(num, i))


linear_search(nums, 3)