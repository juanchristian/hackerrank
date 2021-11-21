input()

lst = [int(n) for n in input().split()]
print(sorted(set(lst))[-2])