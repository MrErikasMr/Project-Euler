def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True




starting_string = '98'

target_length = 9

finishing_string = '7654321'

index = 0
start = 1
big_array = []

list1 = ['7','6','5','4','3','2','1']



def swap_positions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2],list[pos1]

    return ''.join(list)



big_array.append(987654321)

first_number = -2
second_number = -1
while True:
    big_array.append(int('98' + swap_positions(list1,first_number,second_number)))
    second_number -= 1
    print(big_array)

print(big_array)


# while True:
#     new_string = finishing_string[start:] + finishing_string[index]
#     print(new_string)
#     big_array.append(new_string)
#     new_string = ""
#
#     index += 1


