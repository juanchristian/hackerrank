#!/bin/python3

import os
import sys

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    output = []

    for grade in grades:
        if grade < 38:
            output.append(grade)
            continue

        result = divmod(grade, 5)
        if result[1] > 0 and result[1] >= 3:
            new_grade = (result[0] + 1) * 5
            output.append(new_grade)
        else:
            output.append(grade)

    return output

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
