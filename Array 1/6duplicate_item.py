def duplicate_item(nums):
    nums2 = []
    for num in nums:
        if num in nums2:
            return True
        nums2.append(num)

    return False   


    #  start = 0
    #     end = len(nums) -1

    #     if len(nums) == 1:
    #         return False
    #     while start < end:
    #         if nums[start] == nums[end]:
    #             return True
    #         start += 1
    #         end -=1
    #     return False   
        

nums =  [1,2,3,1]     

print(duplicate_item(nums))

