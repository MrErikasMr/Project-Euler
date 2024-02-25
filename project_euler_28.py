def recurring_cycle_length(n):
    # Initialize the remainder to 1
    remainder = 1
    # Initialize the list of remainders
    remainders = []
    # Loop until we find a repeating remainder or the remainder becomes 0
    while remainder != 0 and remainder not in remainders:
        # Add the current remainder to the list of remainders
        remainders.append(remainder)
        # Calculate the next remainder
        remainder = (remainder * 10) % n

    # If the remainder becomes 0, there is no recurring cycle
    if remainder == 0:
        return 0
    # If the remainder is already in the list of remainders, we have found a recurring cycle
    else:
        return len(remainders) - remainders.index(remainder)

# Initialize the maximum recurring cycle length and the corresponding denominator
max_recurring_cycle_length = 0
max_recurring_cycle_denominator = 0

# Loop through all denominators less than 1000
for d in range(2, 1000):
    # Calculate the recurring cycle length for the current denominator
    cycle_length = recurring_cycle_length(d)
    # Update the maximum recurring cycle length and the corresponding denominator if necessary
    if cycle_length > max_recurring_cycle_length:
        max_recurring_cycle_length = cycle_length
        max_recurring_cycle_denominator = d

# Print the result
print(max_recurring_cycle_denominator)



print(1/983)