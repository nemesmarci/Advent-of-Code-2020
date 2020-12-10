def get_jolts():
    jolts = [0]
    with open('input.txt') as data:
        jolts.extend(sorted(list(map(int, data))))
    jolts.append(jolts[-1] + 3)
    return jolts


def get_diffs(jolts):
    return (jolts[i] - jolts[i - 1] for i in range(1, len(jolts)))
