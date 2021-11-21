x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i1, i2, i3] for i1 in range(x + 1) for i2 in range(y + 1) for i3 in range(z + 1) if (i1 + i2 + i3 != n)])