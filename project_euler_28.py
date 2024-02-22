#Find the unit fraction below 1000 with the longest reciprocal
#example: 1/3 = 0.333 (only 1 recurring digit)
# 1/7 = 0.142857142857 (6 digit reucurring)


print(1/7)

recurring_array = []
y_array = []

y = 5
while y < 1001:
    string = str(1 / y)
    if len(string) < 6:
        y += 1
        continue



    for x in range(2,len(string)):
        print(y)


        instance1 = int((x/2) + 1)

        recurring1 = string[2:instance1]
        value = int(x/2)

        recurring2 = string[value + 1: value * 2]

        if recurring1 == recurring2 and len(recurring1) > 5:
            recurring_array.append(recurring1)
            y_array.append(y)
            y += 1
            break
        if x == len(string) - 1:

            y += 1
            break



print(y_array)
print(recurring_array)
print(max(recurring_array))

longest = ""

for z in range(len(recurring_array)):
    if len(recurring_array[z]) > len(longest):
        longest = recurring_array[z]

print(longest)
