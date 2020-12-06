from common import parse_answers

print(sum(v == group[1]
          for group in parse_answers()
          for v in group[0].values()))
