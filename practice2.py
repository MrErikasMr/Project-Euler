from collections import Counter


def solution(directions):

    start_x,start_y = 0,0

    x,y = 0,0


    for move in directions:
        if move == "N":
            y += 1
        elif move == "E":
            x += 1
        elif move == "S":
            y -= 1
        elif move == "W":
            x -= 1
        print(x,y)






print(solution("SxWxNxN"))



