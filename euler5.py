"""<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""

x = 0
count = 20

while x < 1:
    if (count % 2 == 0) and (count % 3 == 0) and (count % 4 == 0) and (count % 5 == 0) and (count % 6 == 0)and (count % 7 == 0) and (count % 8 == 0) and (count % 9 == 0) and (count % 10 == 0) and (count % 11 == 0) and (count % 12 == 0) and (count % 13 == 0) and (count % 14 == 0) and (count % 15 == 0) and (count % 16 == 0) and (count % 17 == 0) and (count % 18 == 0) and (count % 19 == 0) and (count % 20 == 0):
        print(count)
        x += 1
        break

    else:
        count += 20