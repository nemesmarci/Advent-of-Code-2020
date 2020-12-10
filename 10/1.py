from collections import Counter

from common import get_jolts, get_diffs

diffs = Counter(get_diffs(get_jolts()))
print(diffs[1] * diffs[3])
