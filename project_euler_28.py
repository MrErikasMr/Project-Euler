
longest_string = ""
number = 0
for x in range(1,1000):
    #print(1/x)
    num = 1/x
   # print(f"{num:.100f}")
    string_num = str(num)
    #print(string_num)
    if len(string_num) > 6:
        print(string_num)
        print(string_num[3:15])






