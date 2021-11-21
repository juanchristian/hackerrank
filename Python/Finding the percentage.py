total_of_students = int(input())
items = [total_of_students]
means = {}

temp = 0
while temp <= total_of_students:
    items.append(input())
    temp += 1

for item in items[1:-1]:
    temp = item.split()
    name = temp[0]
    grades = temp[1:]
    num_sum = 0
    for grade in grades:
        num_sum += float(grade)
    means[name] = format(num_sum / len(grades), '.2f')
    
print(means[items[-1]])