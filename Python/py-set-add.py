import fileinput

stamps = set()

line_no = 1
for line in fileinput.input():
    if line_no > 1:
        stamps.add(str(line).strip())

    line_no += 1

print(len(stamps))
