import math



factorial1 = math.factorial(4)
total_sum = 0


for x in range(10,100000):

    string = str(x)
    string_sum = 0


    for y in range(len(string)):


        string_sum += math.factorial(int(string[y]))
        if string_sum > x:
            break


    if string_sum == x:
        print(x)
        total_sum += x

print(total_sum)

