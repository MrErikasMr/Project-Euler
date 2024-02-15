

total_sum = 0
for x in range(1,220):

    if 220 % x == 0:
        print(x)
        total_sum += x



print(total_sum)



total_sum2 = 0
for y in range(1,284):
    if 284 % y == 0:
        print(y)
        total_sum2 += y

print(total_sum2)

z = 1
total_sum3 = []
while z < 10001:
    total_sum = 0
    total_sum2 = 0
    total_factors = []
    total_factors2 = []
    for i in range(1,z):
        if z % i == 0:

            total_sum += i

    for n in range(1, total_sum):
        if total_sum % n == 0:
            total_sum2 += n

    if total_sum2 == z and (z != total_sum) and (z or total_sum not in total_sum3):
        a = z,total_sum
        total_sum3.append(z)
        total_sum3.append(total_sum)
        print(z,total_sum)


    z += 1




print(total_sum3)
total_sum3 = set(total_sum3)
print(sum(total_sum3))