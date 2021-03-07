
from collections import namedtuple

num_of_students, students = int(input()), namedtuple('students', input().split())
student_list = [students(*input().split()) for i in range(num_of_students)]
print(sum([float(i.MARKS) for i in student_list])/num_of_students)


