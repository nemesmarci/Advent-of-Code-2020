REQUIRED = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']


def parse_fields(passport):
    return {key: value for key, value
            in map(lambda f: f.split(':'), passport.split())
            if key != 'cid'}


def fields_ok(fields):
    return sorted(fields.keys()) == REQUIRED
