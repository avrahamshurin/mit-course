
import time
import sys



def peak_finder1(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    if nums[0] >= nums[1]:
        return nums[0]

    for i in range(len(nums[:-1])):
        if nums[i-1] <= nums[i] >= nums[i+1]:
            return nums[i]

    return nums.pop()

def peak_finder2(nums):
    if len(nums) == 0:
        return None
    if len(nums) == 1:
        return nums[0]
    high = len(nums)
    low = 0
    i = len(nums)//2
    while True:
        if i == len(nums)-1:
            return nums[i]
        if nums[i - 1] <= nums[i] >= nums[i + 1]:
            return nums[i]
        if nums[i] <= nums[i+1]:
            low = i
            i = (high + low) // 2
        else:
            high = i
            i = (high + low) // 2





t1 = time.time()
print(peak_finder1([i for i in range(int(sys.argv[1]))]))
print("algorithim 1 O(n) : {}".format(time.time()-t1))

t1 = time.time()
print(peak_finder2([i for i in range(int(sys.argv[1]))]))
print("algorithim 2 O(log(n)) : {}".format(time.time()-t1))