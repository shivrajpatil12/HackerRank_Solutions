import string


def main():
    N = int(input())
    alphabet = string.ascii_lowercase[:N]

    height = N * 2 - 1
    width = N * 4 - 3
    lines = [None] * height
    for i in range(N):
        sub_alphabet = alphabet[(-i - 1):]
        letters = ''.join(reversed(sub_alphabet)) + sub_alphabet[1:]
        lines[i] = lines[-i - 1] = '-'.join(letters).center(width, '-')
    print(*lines, sep='\n')


if __name__ == '__main__':
    main()



# import sys
#
# stdin = sys.stdin
#
# n = int(stdin.readline())
# for i in range(2*n-1):
#     d = n-1-abs(n-1-i)
#     for j in range(4*n-3):
#         if j % 2 == 0 and abs((j-(2*n-2))//2) <= d:
#             sys.stdout.write(chr(97+n-1-(d-abs((j-(2*n-2))//2))))
#         else:
#             sys.stdout.write("-")
#     sys.stdout.write("\n")



# def getRangoli(n):
#     r = []
#     letters = [chr(ord('a') + x) for x in range(26)]
#     hold = curr = n - 1
#     for i in range(n):
#         line = ''
#         for j in range(2 * n - 1):
#             if j % 2 == 1:
#                 line += '-'
#             else:
#                 num = (2 * n - 2 - j) // 2 + curr
#                 if num <= hold:
#                     line += letters[num]
#                 else:
#                     line += '-'
#         line = line + line[:-1][::-1]
#         curr -= 1
#         r.append(line)
#     for i in range(n - 2, -1, -1):
#         r.append(r[i][:])
#     return r
