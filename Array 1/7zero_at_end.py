def move_zero_at_end(nums):
    flag = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[flag] = nums[i]
            flag+=1

    while flag < len(nums):
        nums[flag] = 0
        flag += 1  
    
    return nums


nums = [0,1,0,3,12]
print(move_zero_at_end(nums))