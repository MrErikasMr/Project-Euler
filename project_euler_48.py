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
y_start = 0
can_break = False

while True:
    if can_break:
        print(dict1)
        break
    dict1 = {}

    for y in range(y_start,len(prime_array)):
        print(total_sum)
        if total_sum >= 1000:
            y_start += 1
            total_sum = 0
            break

        total_sum += prime_array[y]

        if is_prime(total_sum):
            print('yes')
            dict1[total_sum] = prime_array[:y + 1]
            if total_sum > 990 and total_sum < 1000:
                can_break = True
                break



print(dict1)
print(total_sum)
print(prime_array)