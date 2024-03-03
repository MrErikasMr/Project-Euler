#produce a partition function, and then apply the logic to make up all possibilities to get to £2.00 using pound sterling coins

goal = 5

x = 1
array = []

while sum(array) < goal:
    array.append(1)




a = -2
big_array = []
array2 = []
while True:
    #print(array[a:])
   # print(array)
    var1 = sum(array[a:])
    var2 = (array[0:a])
    var2.append(var1)
   # print(array)
   # print(var2)
    big_array.append(var2)
    print(big_array)
    if big_array[-1][-1] < sum(array):

        a -= 1
    else:
        break








print(big_array)


#start with 1+1+1 until you reach your number
#break this down until it's n-1 + 1
#then, use factors to build up to the number