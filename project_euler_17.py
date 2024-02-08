from num2words import num2words
import re




string1 = ''
for x in range(1,1001):
    string1 += re.sub(r'[ -]', '',num2words((x)))


print(string1)

print(len(string1))

