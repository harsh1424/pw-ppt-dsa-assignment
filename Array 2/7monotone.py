# nums = [1,2,3,2]
# nums2 = nums
# nums.sort()
# print(nums)
# print(nums2)

def monotone(nums):
    inc = True
    dec = True
    for i in range(len(nums) - 1):
        if nums[i] < nums[i+1]:
            dec = False
        if nums[i] > nums[i+1]:
            inc = False

    if inc or dec:
        return True
    else:
        return False    

nums = [1,2,2,3]

print(monotone(nums))