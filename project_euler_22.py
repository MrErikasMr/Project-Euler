#sum of factorials
import math



print(math.factorial(100))



number = str(math.factorial(100))

print(number)

total_sum = 0
for x in range(len(number)):
    total_sum += (int(number[x]))
    print(number[x])


print(total_sum)