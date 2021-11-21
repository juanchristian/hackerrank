import fileinput
from collections import Counter

shoes_counter = None
money_total = 0

line_no = 1
for line in fileinput.input():
    if line_no == 2:
        shoes_counter = Counter(line.split())
    if line_no >= 4:
        shoe_size, price = tuple(line.split())
        if shoe_size in shoes_counter.keys() and shoes_counter[str(shoe_size)] > 0:
            money_total += int(price)
            shoes_counter[str(shoe_size)] -= 1

    line_no += 1

print(money_total)
