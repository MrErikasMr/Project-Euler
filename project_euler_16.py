

power = 1000




print(len(str(2**1000)))
number_actual = str(2**1000)
number = len(str(2**1000))

total_sum = 0

for x in range(number):

    total_sum += int(number_actual[x])
    print(number_actual[x])


print(total_sum)