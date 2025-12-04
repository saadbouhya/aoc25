# 234234234234278
# 434234234278


def get_max_joltage(joltages: str):
    res = []
    joltages = [int(c) for c in joltages]
    size = len(joltages)
    # max index each time
    while True:
        # Calculate how many elements to consider from the start
        i = len(joltages) - (12 - len(res))
        if len(res) == 12:
            break
        if i <= 0:
            res.extend(joltages)
            break
        print("i (number of elements to consider):", i)

        # Find the maximum value among the first i+1 elements
        max_ = max(joltages[: i + 1])

        # Append the maximum value to the result list
        res.append(max_)

        # Remove all elements up to and including the found maximum
        joltages = joltages[joltages.index(max_) + 1 :]

        # Debug prints
        print("Current maximum selected:", max_)
        print("Remaining joltages:", joltages)
        print("Result list so far:", res)

        # Pause the loop for step-by-step inspection
        # input("Press Enter to continue...")
    print(int("".join([str(i) for i in res])))
    return int("".join([str(i) for i in res]))


def main():
    total = 0
    with open("input.txt", "r") as f:
        count = 0
        for line in f:
            print(f"Line {count}")
            total += get_max_joltage(line.strip())
            count += 1
    print(total)


if __name__ == "__main__":
    main()
