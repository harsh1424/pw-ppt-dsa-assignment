def candy_type_to_eat(candy_type):
    total_candies = len(candy_type)
    unique_candy_type = []
    for i in range(len(candy_type)):
        if candy_type[i] not in unique_candy_type:
            unique_candy_type.append(candy_type[i])

    unique_candies = len(unique_candy_type)

    if unique_candies <= total_candies/2:
        return unique_candies
    else:
        return int(total_candies/2)
    

candy_type = [1,1,2,2,3,3]   
print(candy_type_to_eat(candy_type)) 