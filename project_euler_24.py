import os
import re

file_name = 'problem 18/names.txt'



with open(file_name, 'r') as file:
    # Read the file into a list of lines
    lines = file.readlines()
    content1 = file.read()
    print(content1)





array = []

#print(lines[0])

alphabet = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"

array2 = []
for x in range(len(lines[0])):
    if lines[0][x] != '"':
        array.append(lines[0][x])

print(array)
string = ""
for y in range(len(array)):

    if array[y] != ',':
        string += array[y]
    else:
        array2.append(string)

        string = ""


#print(array)
array3 = sorted(array2)
print(array3)

array4 = ["a"]

total_sum1 = 0


total_sum_total = 0
for n in range(len(array3)):
   # print(array3[n])

    # if array3[n] == "COLIN":
    #     print(array3[n])
    #     print(n)
    #     for z in range(len(array3[n])):
    #         total_sum1 += alphabet.index(array3[n][z])
    #
    #     print(total_sum1)
    #     print(total_sum1 * n)
    #
    #     break
  #  print(array3[n])
    total_sum = 0
    for x in range(len(array3[n])):
     #   print(array3[n][x])
      #  print(alphabet.index(array3[n][x]))
        total_sum += alphabet.index(array3[n][x])

    total_sum_total += (total_sum * n)
print(total_sum_total)

print(len(array2))

print(len(array3))

print(array)
print(array3)

print(array3.index('COLIN'))