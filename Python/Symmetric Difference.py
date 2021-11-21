input()
lst1 = map(int, input().split())
input()       
lst2 = map(int, input().split())

set1 = set(lst1)
set2 = set(lst2)
only1 = set1.difference(set2)
only2 = set2.difference(set1)
final = only1.union(only2)
for n in sorted(list(final)):
    print(n)