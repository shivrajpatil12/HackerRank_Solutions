eng_students = input()
eng_roll_numbers = set(list(input().split()))
french_student = input()
french_roll_number = set(input().split())

print(len(eng_roll_numbers.union(french_roll_number)))