def place_flower(flowerbed, n):
    count = 0
    # left_empty = False
    # right_empty = False
    for i in range(len(flowerbed)):
        left_empty = False
        right_empty = False
        if flowerbed[i] == 0:
            if i == 0 or flowerbed[i-1] == 0:
                left_empty = True

            if i == len(flowerbed) - 1 or flowerbed[i+1] == 0:
                right_empty = True


            if left_empty and right_empty :
                flowerbed[i] = 1
                count += 1

    return count >= n 


flowerbed = [1,0,0,0,1]
n = 1
print(place_flower(flowerbed, n))


flowerbed = [1,0,0,0,1]
n = 2
print(place_flower(flowerbed, n))