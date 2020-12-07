import re

from common import fields_ok, parse_fields

HGT = re.compile(r'^(\d+)(cm|in)$')
HCL = re.compile(r'^#[0-9a-f]{6}$')
PID = re.compile(r'^[0-9]{9}$')


def hgt_ok(hgt):
    if not(hgt := re.match(HGT, hgt)):
        return False
    num = int(hgt.group(1))
    unit = hgt.group(2)
    return 150 <= num <= 193 if unit == 'cm' else 59 <= num <= 76


def year_ok(year, _min, _max):
    return len(year) == 4 and _min <= int(year) <= _max


def byr_ok(byr):
    return year_ok(byr, 1920, 2002)


def iyr_ok(iyr):
    return year_ok(iyr, 2010, 2020)


def eyr_ok(eyr):
    return year_ok(eyr, 2020, 2030)


def hcl_ok(hcl):
    return re.match(HCL, hcl) is not None


def ecl_ok(ecl):
    return ecl in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


def pid_ok(pid):
    return re.match(PID, pid) is not None


with open('input.txt') as data:
    print(sum(fields_ok(fields) and
              byr_ok(fields['byr']) and
              iyr_ok(fields['iyr']) and
              eyr_ok(fields['eyr']) and
              hgt_ok(fields['hgt']) and
              hcl_ok(fields['hcl']) and
              ecl_ok(fields['ecl']) and
              pid_ok(fields['pid'])
              for fields in map(parse_fields, data.read().split('\n\n'))))
