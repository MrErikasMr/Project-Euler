from curses.ascii import isdigit
from collections import Counter

player_1 = '5H 5C 6S 7S KD'
player_2 = '2C 3S 8S 8D TD'
rank_numbers = [0, 3, 6, 9, 12]





def rule_pairs():
    rank_array1 = []
    rank_array2 = []
    for x in range(len(player_1)):
        if x not in rank_numbers:
            continue
        else:
            rank_array1.append(player_1[x])
            rank_array2.append(player_2[x])
    count1 = Counter(rank_array1)
    count2 = Counter(rank_array2)
    duplicates1 = {key: value for key, value in count1.items() if value > 1}
    duplicates2 = {key: value for key, value in count2.items() if value > 1}

    print("Duplicates:", duplicates1)
    print("Duplicates:", duplicates2)






def rule_high_card():
    highest_card_1 = []
    highest_card_2 = []
    dict = {'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14}

    for x in range(len(player_1)):
        if x not in rank_numbers:
            continue
        else:
            if isdigit(player_1[x]):
                highest_card_1.append(int(player_1[x]))
            else:
                print(player_1[x])
                print(dict[player_1[x]])
                highest_card_1.append(dict[player_1[x]])
                continue



    for x in range(len(player_2)):
        if x not in rank_numbers:
            continue
        else:
            if isdigit(player_2[x]):
                highest_card_2.append(int(player_2[x]))
            else:
                print(player_2[x])
                print(dict[player_2[x]])
                highest_card_2.append(dict[player_2[x]])
                continue


    highest_card_1 = highest_card_1[-1]
    highest_card_2 = highest_card_2[-1]
    print("high card 1: ", highest_card_1)
    print("high card 2: ", highest_card_2)






def card_creator():
    suits = ['S','C','H','D']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    cards = []

    for x in range(len(ranks)):
        for y in range(len(suits)):
            string = ranks[x] + suits[y]
            cards.append(string)




card_creator()
rule_high_card()
rule_pairs()