def parse():
    with open('input.txt') as data:
        deck1, deck2 = map(lambda x: x.split('\n'), data.read().split('\n\n'))
        deck1, deck2 = list(map(int, deck1[1:])), list(map(int, deck2[1:-1]))
        return deck1, deck2


def solve(game):
    deck1, deck2 = parse()
    game(deck1, deck2)
    winner = deck1 if len(deck1) else deck2
    size = len(winner)
    return(sum((size - i) * card for i, card in enumerate(winner)))
