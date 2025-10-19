"""<p>Starting with the number $1$ and moving to the right in a clockwise direction a $5$ by $5$ spiral is formed as follows:</p>
<p class="monospace center"><span class="red"><b>21</b></span> 22 23 24 <span class="red"><b>25</b></span><br>
20  <span class="red"><b>7</b></span>  8  <span class="red"><b>9</b></span> 10<br>
19  6  <span class="red"><b>1</b></span>  2 11<br>
18  <span class="red"><b>5</b></span>  4  <span class="red"><b>3</b></span> 12<br><span class="red"><b>17</b></span> 16 15 14 <span class="red"><b>13</b></span></p>
<p>It can be verified that the sum of the numbers on the diagonals is $101$.</p>
<p>What is the sum of the numbers on the diagonals in a $1001$ by $1001$ spiral formed in the same way?</p>
"""


spiral_end = 1001**2



##top right formula = 4 * N^2 - 4N - 1
## --> (1002001 - 1 + 4N)

##root is 501 therefore 501 * 2 is the length of one diagonal, and 501*2 of the other diagonal

n = 500

diagonal_top_right_end = (4 * n**2) - (4 * n) + 1
print(diagonal_top_right_end)

diagonal_bottom_left_end = (4 * n ** 2) + 1
print(diagonal_bottom_left_end)

diagonal_top_left_end = (4 * n ** 2) + (2 * n) + 1
print(diagonal_top_left_end)

diagonal_bottom_right_end = (4 * n ** 2) - (2*n) + 1
print(diagonal_bottom_right_end)

sum2 = 0
for x in range(n + 1):
    sum1 = (4 * x**2) - (4 * x) + 1
    print((4 * x**2) - (4 * x) + 1)
    sum2 += sum1
    sum1 = 0


print(diagonal_top_right_end)


for x in range(n + 1):
    sum1 = (4 * x ** 2) + 1
    print((4 * x ** 2) + 1)
    sum2 += sum1
    sum1 = 0


print(diagonal_bottom_left_end)


for x in range(n + 1):
    sum1 = (4 * x ** 2) + (2 * x) + 1
    print((4 * x ** 2) + (2 * x) + 1)
    sum2 += sum1
    sum1 = 0



print(diagonal_top_left_end)



for x in range(n + 1):
    sum1 = (4 * x ** 2) + (2*x) + 1
    print((4 * x ** 2) + (2*x) + 1)

    sum2+= sum1
    sum1 = 0


print(diagonal_bottom_right_end)

print(sum2)


side = 1001
layers = (side - 1) // 2  # 500
total = 1
for k in range(1, layers + 1):
    total += (4*k*k + 4*k + 1)  # top-right
    total += (4*k*k + 2*k + 1)  # top-left
    total += (4*k*k + 1)        # bottom-left
    total += (4*k*k - 2*k + 1)  # bottom-right



print(total)