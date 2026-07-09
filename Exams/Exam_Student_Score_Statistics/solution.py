def mean(lst):
    return sum(lst) / len(lst)


def sd(lst):
      if len(lst) == 1:
          return 0

      m = mean(lst)
      s = 0

      for score in lst:
          s += (m - score) ** 2

      s /= len(lst) - 1
      return s ** 0.5


def mode(lst):
    my_dict = {}

    for score in lst:
        my_dict[score] = my_dict.get(score, 0) + 1

    best_score = None
    best_count = -1

    for score in my_dict:
        if my_dict[score] > best_count:
            best_count = my_dict[score]
            best_score = score

        elif my_dict[score] == best_count and score < best_score:
            best_score = score

    return best_score



def main():
    n = int(input())
    nums = []

    for _ in range(n):
        score = int(input())

        if score < 0 or score > 100:
            continue

        nums.append(score)


    if len(nums) == 0:
        print("No valid score")
        return

    print(f"{mean(nums):.2f}")
    print(f"{sd(nums):.2f}")
    print(mode(nums))


if __name__ == "__main__":
    main()
