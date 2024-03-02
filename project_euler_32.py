#produce a partition function, and then apply the logic to make up all possibilities to get to £2.00 using pound sterling coins

x = 1

while True:

    if x >= 5:
        break

#start with 1+1+1 until you reach your number
#break this down until it's n-1 + 1
#then, use factors to build up to the number