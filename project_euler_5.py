"""<p>$2520$ is the smallest number that can be divided by each of the numbers from $1$ to $10$ without any remainder.</p>
<p>What is the smallest positive number that is <strong class="tooltip">evenly divisible<span class="tooltiptext">divisible with no remainder</span></strong> by all of the numbers from $1$ to $20$?</p>
"""


counter = 2
counter_has_reached = False


while True:
    if counter_has_reached:
        print(counter)
        break
    counter += 1
    for x in range(2, 21):

        if counter % x == 0:
           # print(x)
            if x == 20:
                counter_has_reached = True
                break

            continue
        else:
            break

