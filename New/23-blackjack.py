# example of a blackjack game

import random

suits = ["hearts", "spades", "clubs", "diamonds"]
# ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
ranks = [{ "rank": "A", "value": 11 },
         { "rank": "2", "value": 2 },
         { "rank": "3", "value": 3 },
         { "rank": "4", "value": 4 },
         { "rank": "5", "value": 5 },
         { "rank": "6", "value": 6 },
         { "rank": "7", "value": 7 },
         { "rank": "8", "value": 8 },
         { "rank": "9", "value": 9 },
         { "rank": "10", "value": 10 },
         { "rank": "J", "value": 10 },
         { "rank": "Q", "value": 10 },
         { "rank": "K", "value": 10 }]

# for suit in suits:
#   for rank in ranks:
#     print([suit, rank])
cards = [[suit, rank] for suit in suits for rank in ranks]


def shuffle():
    random.shuffle(cards)


def deal(number):
    # return cards.pop()
    # cards_dealt = []
    # for x in range(number):
    #   cards_dealt.append(cards.pop())
    # return cards_dealt
    return [cards.pop() for _ in range(number)]


shuffle()
# cards_dealt = deal(2)
# card = cards_dealt[0]
# rank = card[1]

# if rank == "A":
#     value = 11
# elif rank in ["J", "Q", "K"]:
#     value = 10
# else:
#     value = int(rank)

# rank_dict = { "rank": rank, "value": value }

# print(rank_dict["rank"], rank_dict["value"])

card = deal(1)[0]

print(card)