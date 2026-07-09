def is_perfect(num):
    if (num < 2):
        return False

    s = 1
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            s += i

            pair = num // i
            if pair != i:
                s += pair

    return s == num


def main():
    limit = int(input())
    p = False

    for i in range(1, limit + 1):
        if (is_perfect(i)):
            print(i)
            p = True

    if (not p):
        print("No perfect number.")

if __name__ == "__main__":
    main()
