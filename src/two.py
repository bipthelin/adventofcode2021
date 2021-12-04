def main():
    file = open("input/2.data", "r")

    # Part 1
    horizontal = 0
    depth = 0

    for line in file.readlines():
        command = line.split()
        if command[0] == "forward":
            horizontal += int(command[1])
        elif command[0] == "down":
            depth += int(command[1])
        elif command[0] == "up":
            depth -= int(command[1])

    print("Part 1: "+str(horizontal * depth))

    file.seek(0)

    # Part 2
    aim = 0
    horizontal = 0
    depth = 0

    for line in file.readlines():
        command = line.split()
        if command[0] == "forward":
            horizontal += int(command[1])
            depth += aim * int(command[1])
        elif command[0] == "down":
            aim += int(command[1])
        elif command[0] == "up":
            aim -= int(command[1])

    print("Part 2: "+str(horizontal * depth))

if __name__ == "__main__":
    main()
