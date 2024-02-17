##non abundant sums


big_array = []
for x in range(1, 100):
    #print(x,"x")
    factor_array = []
    for i in range(1,x):
        if x % i == 0:
            factor_array.append(i)
            #print(i)

    if sum(factor_array) > x:
        print(x, "YO")
        big_array.append(x)

print(big_array)


for y in range(1,big_array[-1]):
    for z in range(1,big_array[-1]):
        # find all the numbers that are smaller than let's say "40" and then create an array of all those numbers
    # and then try to add those numbers together 1 by 1, and if we get a sum that is bigger, move onto the next integer



