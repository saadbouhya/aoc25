def get_max_joltage(joltages: str):
    val = -1 
    # get first element
    first = -1
    for i in range(13):
        if int(joltages[i]) > first:
            first = joltages[i]
            i_first = i

    for i in range(i_first + 1, 13):


    for i in range(len(joltages)):
        for k in range(i + 1, len(joltages)):
            if int(f"{joltages[i]}{joltages[k]}") > val:
                val = int(f"{joltages[i]}{joltages[k]}")
    return val
            

def main():
    total = 0
    with open("input.txt", "r") as f:
        for line in f:
            total += get_max_joltage(line.strip())
    print(total)


if __name__ == "__main__":
    main()