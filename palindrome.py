def solution(input):
    solution = ""
    for x in range(len(input)):
        for y in range(min(x + 1, len(input) - x)):
            if input[x - y] != input[x + y]:
                break
        current = input[x - y: x + y + 1]
        if len(current) > len(solution):
            solution = current

        for y in range(min(x + 1, len(input) - x - 1)):
            if input[x - y] != input[x + y + 1]:
                break
            current = input[x - y: x + y + 2]
            if (len(current) > len(solution)):
                solution = current

    return solution


print(solution("bob has a racecar and a bike"))