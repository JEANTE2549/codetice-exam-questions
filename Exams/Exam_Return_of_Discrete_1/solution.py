def main():
    binary = input()
    decimal = 0

    for digit in binary:
        decimal = decimal * 2 + int(digit)

    print(decimal)


if __name__ == "__main__":
    main()
