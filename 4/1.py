from common import fields_ok, parse_fields

with open('input.txt') as data:
    print(sum(fields_ok(parse_fields(passport))
              for passport in data.read().split('\n\n')))
