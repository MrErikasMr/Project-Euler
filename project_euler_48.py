"""consecutive_prime_sums"""



def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True



limit = 1000000

prime_array = []
x = 0
while True:

    if sum(prime_array) > limit:
        break

    if is_prime(x):
        prime_array.append(x)
    x += 1



total_sum = 0
y_start = 0
can_break = False




print(prime_array)


prime_indices = []


x = 0
start_x = 0
array_of_primes = []
while True:
    try:

        total_sum += prime_array[x]
        if is_prime(total_sum):
            print(total_sum)
            array_of_primes.append(prime_array[start_x: x + 1])
            print(prime_array[start_x])

        if total_sum >= limit:
            start_x += 1
            x = start_x
            total_sum = 0
            continue
        x += 1
    except IndexError:
        break


print(array_of_primes)

longest_array = max(array_of_primes,key=len)

print(max(array_of_primes,key=len))



print(sum(longest_array))
print(len(longest_array))
# print(prime_array[:])
# total_sum = 0
# for x in range(len(prime_array[:14])):
#     total_sum += prime_array[x]
#     print(prime_array[x])
#
# print(total_sum)
#
# print(is_prime(total_sum))