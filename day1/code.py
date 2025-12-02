# arrow 0 -> 99
# same as dial of a clock
# can rotate left or right
# right is clockwise
# starting position is 50


def calculate_position(start, rotation):
    position = start
    rotation_direction = rotation[0]
    rotation_amount = int(rotation[1:])
    hundreds = rotation_amount // 100
    rotation_amount = rotation_amount % 100
    if rotation_direction == "L":
        position = position - rotation_amount
        if position == 0:
            if start != 0:
                hundreds += 1
        if position < 0:
            if start != 0:
                hundreds += 1
            position = 100 - abs(position)
    elif rotation_direction == "R":
        position = position + rotation_amount
        if position == 0:
            if start != 0:
                hundreds += 1
        if position > 99:
            position = position - 100
            if start != 0:
                hundreds += 1
    print(f"Start: {start}, New Position: {position}, Hundreds: {hundreds}")
    return position, hundreds


def main():
    with open("input.txt") as f:
        rotations = [line.strip() for line in f if line.strip()]

    # rotations = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]

    count = 0
    for i, r in enumerate(rotations):
        if i == 0:
            position, plus = calculate_position(50, r)
        else:
            position, plus = calculate_position(position, r)
        count += plus
    print(count)

if __name__ == "__main__":
    main()
