from common import solve


def standard(deck1, deck2):
    while len(deck1) and len(deck2):
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        elif card2 > card1:
            deck2.append(card2)
            deck2.append(card1)


print(solve(game=standard))
