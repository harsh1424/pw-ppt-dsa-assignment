def search_index(nums, target):
    left = 0
    right = len(nums)

    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid
        else:
            left = mid + 1
        
    return left

nums = [1,3,5,6]
target = 5

print(search_index(nums, target))