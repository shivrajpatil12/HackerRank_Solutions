# #!/usr/bin/python
#
# t = int(input())
#
# stus = {}
#
# for i in range(0, t):
#     name, math, physic, chemistry = input().split(" ")
#     stus[name] = (float(math) + float(physic) + float(chemistry)) / 3
#
# name = input()
# if name in stus:
#     print("%.2f" % stus[name])
# else:
#     print("No")
#

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = sum(scores)/3
        # student_marks[name] = scores
    query_name = input()

    if query_name in student_marks.keys():
        print("%.2f" % student_marks[query_name])
