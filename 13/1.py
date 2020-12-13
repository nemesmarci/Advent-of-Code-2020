from common import parse

timestamp, buses = parse()

min_wait = min_id = None

for _, bus_id in buses:
    departs = timestamp - timestamp % bus_id + bus_id
    wait = departs - timestamp
    if min_wait is None or wait < min_wait:
        min_wait = wait
        min_id = bus_id

print(min_id * min_wait)
