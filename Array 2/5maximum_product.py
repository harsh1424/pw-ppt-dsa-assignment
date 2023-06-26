def maximum_product(nums):
    nums.sort()
    all_positive = nums[-1]*nums[-2]*nums[-3]
    if_negative = nums[0]*nums[1]*nums[-1]
    return max(all_positive, if_negative)


nums = [1,2,3]
print(maximum_product(nums))







# print(nums[-1])
# print(nums[-2])


#  if there is negetive number we have to look for that also 
#  largest negaive num * largest negative number * largest positive number then we get positive number