x = 3

prime_array = [2]
sum = 0
while len(prime_array) < 2000000:
    for y in range(len(prime_array)):

        if x % prime_array[y] == 0:
            break

        if y == len(prime_array) - 1:
            sum += x
            prime_array.append(x)

            break

    x += 1
print("The sum of the first 2,000,000 prime numbers: ", sum)


