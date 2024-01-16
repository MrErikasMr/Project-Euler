"""<p>By listing the first six prime numbers: $2, 3, 5, 7, 11$, and $13$, we can see that the $6$th prime is $13$.</p>
<p>What is the $10\,001$st prime number?</p>
"""


x = 3

prime_array = [2]
while len(prime_array) < 10001:
    for y in range(len(prime_array)):

        if x % prime_array[y] == 0:
            break

        if y == len(prime_array) - 1:
            prime_array.append(x)

            break

    x += 1





print("10001st prime: ", prime_array[-1])



