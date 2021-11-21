import textwrap

string = str(input())
width = int(input())

print(textwrap.fill(string, width))