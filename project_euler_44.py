
big_array = []
for x in range(1000000000,10000000000):
    string = str(x)
    new_string = ""
    broken = False
    for y in range(len(string)):
        while True:

            if string[y] not in new_string:
                new_string += string[y]
            else:
                broken = True

                print("broken")
                break

        if broken:
            break
        else:


            big_array.append(x)
            print(big_array)
            break



