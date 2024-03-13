def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True




starting_number = 987654321


while starting_number > 100000000:
    string = ""
    if '0' in str(starting_number) or (starting_number % 2 == 0):
        starting_number -= 1
        continue
    string_number = str(starting_number)
    for x in range(len(string_number)):
        if (string_number[x]) not in string:
            string += (string_number[x])
           # print(string)
        else:

            break
    if len(string) == 9 and '0' not in string:
        print(string)
        if is_prime(int(string)):

            print(string)
            break



    #print(starting_number)
    starting_number -= 1


