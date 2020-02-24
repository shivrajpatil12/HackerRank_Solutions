
# physics_students = []
#
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     physics_students.append([name, score])

physics_students = [['Harry', 37.21], ['Berry', 37.11], ['Tina', 37.11], ['Akriti', 41], ['Harsh', 39]]

physics_students.sort()
N = len(physics_students)

# Removing the lowest grades
grades = []
for i in range(N):
    grades.append(physics_students[i][1])
grades.sort()
min_grade = min(grades)
grades_list_temp = grades[:]

for i in range(len(grades)):
    if grades[i] == min_grade:
        print(grades_list_temp[0])
        grades_list_temp.pop(0)
    else:
        pass

# Finding out the names of students with second lowest grade
lowest2nd_names_list = []
for i in range(N):
    if physics_students[i][1] == grades_list_temp[0]:
        print(grades_list_temp[0])
        lowest2nd_names_list.append(physics_students[i][0])

for name in lowest2nd_names_list:
    print(name)