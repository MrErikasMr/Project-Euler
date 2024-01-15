"""<p>A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is $9009 = 91 \times 99$.</p>
<p>Find the largest palindrome made from the product of two $3$-digit numbers.</p>
"""


multiplication_array = []

for x in range(100,1000):
    for y in range(100,1000):
        multiplication = x * y

        if(str(multiplication)[::-1]) == str(multiplication):
            multiplication_array.append(multiplication)


print(max(multiplication_array))


       # print(x * y)