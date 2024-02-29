
a = 2
b = 2
array = []
while True:

    if b > 100:
        break
   # print(a ** b)
    result = a ** b
    if result not in array:
        array.append(result)
    if a < 100:
        a += 1
    else:
        a = 2
        b += 1





print(array)

print(len(array))

