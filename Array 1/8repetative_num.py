def find_repetative_no(nums):
    # n = 1
    # for i in range(len(nums)):
    #     if nums[i] != n:
    #         return [nums[i], n]
    #     n += 1
    # return -1
    new_nums = []
    dulplicate = 0
    missing = 0

    for num in nums:
        if num in new_nums:
            dulplicate = num
        new_nums.append(num)

    for i in range(1, len(nums) + 1):
        if i not in new_nums:
            missing = i
            break


    return [dulplicate, missing]




nums = [1,2,2,4]
print(find_repetative_no(nums))

nums = [1,2,3,4,2,6,7]
print(find_repetative_no(nums))

nums2 = [3,2,2]
print(find_repetative_no(nums2))