def print_formatted(number):
    width = len(str(bin(number)).replace('0b', ''))
    for i in range(1, number + 1):
        decimal = str(i).rjust(width, ' ')
        binary = bin(i)[2:].rjust(width, ' ')
        octal = oct(i)[2:].rjust(width, ' ')
        hexdecimal = hex(i)[2:].rjust(width, ' ').upper()
        print(decimal, octal, hexdecimal, binary)


if __name__ == "__main__":
    n = 16
    print_formatted(n)
