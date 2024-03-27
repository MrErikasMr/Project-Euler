"""consecutive_prime_sums"""



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True



dict1 = {}

prime_array = []

for x in range(1,1000):

    print(is_prime(x))
    if is_prime(x):
        prime_array.append(x)



total_sum = 0
for y in range(len(prime_array)):

    total_sum += prime_array[y]

    if is_prime(total_sum):
        print('yes')
        dict1[total_sum] = prime_array[:y + 1]


print(dict1)
print(total_sum)
print(prime_array)