import numpy as np

array1 = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]




# for x in range(len(array)):
#     print(max(array[x]))
#

# print(array[5])
# print(max(array[5][1:3]))
#



x = 0
array2 = []
array = array1[-2]
z = -1
while x < len(array):
    first_array = array[x]
    second_array = array1[z]
  # print(first_array)
   # print(second_array)


    number1 = first_array + second_array[x]
    number2 = first_array + second_array[x+1]

    actual_number = max(number1,number2)
    x+= 1
    print(actual_number)
    array2.append(actual_number)

    print(array)
    if x == len(array):
        print("hot here")
        array.append(array2)
        x = 0
        z -= 1
        array2 = 0







print(array2)



