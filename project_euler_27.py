# Find the first fibonnaci number to contain 1000 digits





array = [1,1]
number = 0
x = 3
while True:
    number = sum(array)
    array.pop(0)
    array.append(number)
    if len(str(array[-1])) >= 1000:
        print(array)
        print("index of first fibonnacci number with length of 1000 digits or more is: ",x)

        break
    x += 1






