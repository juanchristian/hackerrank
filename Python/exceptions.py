import fileinput

line_no = 1
for line in fileinput.input():
    if line_no > 1:
        a, b = tuple(line.split())
        try:
            print int(int(a) / int(b))
        except Exception as err:
            print "Error Code: " + str(err)

    line_no += 1
