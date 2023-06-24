def plus_one(digits):
    num = 0
    for digit in digits:
        num = num*10 + digit
    num += 1

    num_str = str(num)
    resulting_nums = []
    for num_s in num_str:
        resulting_nums.append(int(num_s))

    return resulting_nums
  







nums = [1,2,3]
print(plus_one(nums))