
a = 0

for x in range(1,1000001):

    string = str(x)
    sum = 0
    for y in range(len(string)):
        sum += int(string[y])**5
    if str(sum) == string:
        print(string)
        a += int(sum)



print("sum",a)