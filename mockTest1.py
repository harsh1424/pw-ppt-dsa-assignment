def moveZeroes(nums):
       
        flag = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[flag] = nums[i]
                flag+=1

        while flag < len(nums):
            nums[flag] = 0
            flag += 1
