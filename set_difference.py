# 9
# 1 2 3 4 5 6 7 8 9
# 9
# 10 1 2 3 11 21 55 6 8

eng_students = set()
n = int(input().strip())
student = set(map(int, input().split()))

r = int(input().strip())
frh_student = set(map(int, input().split()))

print(len(student.difference(frh_student)))
