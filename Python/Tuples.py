num_of_numbers = int(input())
numbers = tuple([int(n) for n in input().split()])
print(hash(numbers))