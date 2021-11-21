a = int(raw_input())
b = int(raw_input())
m = int(raw_input())

if (a >= 1 and a <= 10) and (b >= 1 and b <= 10) and (m >= 2 and m <= 1000):
    print pow(a, b)
    print pow(a, b, m)