




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

# array2 = []
# x = 2
# y = x - 1
# while True:
#
#
#     number = 5**x * 2**y
#
#     for z in range(1, number + 1):
#         if number % z == 0:
#             array2.append(z)
#
#     print(number)
#     print(len(array2))
#
#     if len(array2) >= 500:
#         break
#     else:
#         x += 1
#         y += 1
#
#


x = 0
yes_array = []
no_array = []
while True:
    x += 1

    sum += x

    if sum % x == 0:
        yes_array.append(sum)
        print(x, ":", sum,"yes")

    else:
        no_array.append(sum)
        print(x, ":", sum)



    if x > 20:
        break


print(len(yes_array))
print(len(no_array))

yes_array2 = []
no_array2 = []
biggest_yes_length = 0
biggest_no_length = 0
biggest_yes_index = 0
biggest_no_index = 0
for y in range(1,len(yes_array)):
    for z in range(1,len(yes_array)):
        print(yes_array[z])





print(yes_array)
print(biggest_yes_length, "yo")


sum = 0
sum_array = []
for q in range(1,100):

    sum += q
    sum_array.append(sum)
    #print(sum)

#print(sum_array)



result_dict = {value: None for value in sum_array}



for i in range(len(sum_array)):
    #print(sum_array[i])
    x = 1

    count = 0
    while True:

        if sum_array[i] % x == 0:
            count += 1
            result_dict[sum_array[i]] = count



        if x == sum_array[i]:
            count = 0
            break
        x += 1




# Print the resulting dictionary
print(result_dict)


print(result_dict)



for a in range(1, 501):
    if 500 % a == 0:
        print(a)


print(25*20)

print(2**24 * 2**19)


a = 500
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
x = 0


prime_array = []
while True:
    print(a)
    if a<= 1:
        break
    if (a % primes[x]) != 0:
        x += 1
        continue
    else:
        a = int(a / primes[x])
        print(a, primes[x])
        prime_array.append(primes[x])
        x = 0
        print(prime_array)






print(prime_array)