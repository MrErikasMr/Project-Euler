# Open and read the file
with open("0022_names.txt") as f:
    file = f.read()

# Split the names into a list, stripping quotes
names = file.replace('"', '').split(',')
print(names)
names.sort()

# Define alphabet for scoring
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Calculate total score
total_score = 0
for index, name in enumerate(names, start=1):
    name_value = sum(alphabet.index(letter) + 1 for letter in name)
    total_score += name_value * index

print("Total sum:", total_score)

print("COLIN position:", names.index("COLIN") + 1)