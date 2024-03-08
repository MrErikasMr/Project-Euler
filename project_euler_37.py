#palindromic base-10 and binary numbers


big_array = []


for x in range(1000000):


    string_binary = str(bin(x))
    string_binary = string_binary[2:]
    string_binary_mirror = string_binary[::-1]


    string_number = str(x)
    string_number_mirror = string_number[::-1]

    if string_binary == string_binary_mirror and string_number == string_number_mirror:
        print(string_binary)
        print(string_number)
        big_array.append(x)



print(big_array)

print(sum(big_array))













