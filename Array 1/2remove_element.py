def remove_element(nums, val):
    start = 0
    end = len(nums)-1

    while start <= end:
        if nums[start] == val:
            nums[start], nums[end] = nums[end], nums[start]
            end -= 1
        else:
            start += 1

    return start        


nums = [3,2,2,3]
val = 3

print(remove_element(nums, val))