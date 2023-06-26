def array_pair_sum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum    

    # (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4 sorted array
    # for i in range(1, 6, 2):
    #     print(i)


nums = [1,4,3,2]
print(array_pair_sum(nums))