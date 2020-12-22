from common import solve


def recursive(deck1, deck2):
    previous = set()
    while len(deck1) and len(deck2):
        if (current := (tuple(deck1), tuple(deck2))) in previous:
            return 1
        else:
            previous.add(current)
            card1 = deck1.pop(0)
            card2 = deck2.pop(0)
            if len(deck1) >= card1 and len(deck2) >= card2:
                winner = recursive(deck1[:card1], deck2[:card2])
            else:
                winner = 1 if card1 > card2 else 2
            if winner == 1:
                deck1.append(card1)
                deck1.append(card2)
            else:
                deck2.append(card2)
                deck2.append(card1)
    return 1 if len(deck1) else 2


print(solve(game=recursive))
