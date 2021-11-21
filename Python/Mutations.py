string = input()
pos, char = tuple(input().split())

print(string[:int(pos)] + char + string[int(pos) + 1:])