from operator import itemgetter

number_of_students = int(input())
students = []

temp = 0
while temp < number_of_students:
    students.append([input(), float(input())])
    temp += 1

students.sort(key = itemgetter(1))
grades = set()
for student in students:
    grades.add(student[1])
second_lowest = sorted(list(grades))[1]

bad_students = []
for student in students:
    if student[1] == second_lowest:
        bad_students.append(student[0])
        
for student in sorted(bad_students):
    print(student)