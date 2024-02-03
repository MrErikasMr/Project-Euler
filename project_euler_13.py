




a = 2**249
b = 2**1


#print(a*b)

c = a*b

#x = 0
sum = 0
# while sum <= c:
#     x += 1
#
#     sum += x
#
#     print(sum)
#
# array = []
# for x in range(1,50001):
#
#     if 50000 % x  == 0:
#         array.append(x)
#         print(x)
#
#     print(len(array))
#

array2 = []
x = 2
y = x - 1
while True:


    number = 5**x * 2**y

    for z in range(1, number + 1):
        if number % z == 0:
            array2.append(z)

    print(number)
    print(len(array2))

    if len(array2) >= 500:
        break
    else:
        x += 1
        y += 1




