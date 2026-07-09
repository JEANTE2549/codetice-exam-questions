def factorial(num):
    result = 1

    for i in range(2, num + 1):
        result *= i

    return result


def main():
    n, r = input().split()
    n = int(n)
    r = int(r)

    combination = factorial(n) // (factorial(r) * factorial(n - r))
    permutation = factorial(n) // factorial(n - r)

    print(combination)
    print(permutation)


if __name__ == "__main__":
    main()
