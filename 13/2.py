from common import parse
from chinese_remainder import chinese_remainder

_, data = parse()
rems = [div - rem for rem, div in data]
divs = [div for _, div in data]

print(chinese_remainder(divs, rems))
