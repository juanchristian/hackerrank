import re
import fileinput

line_no = 1
for line in fileinput.input():
    if line_no > 1:
        try:
            re.compile(str(line))
            print(True)
        except re.error:
            print(False)

    line_no += 1
