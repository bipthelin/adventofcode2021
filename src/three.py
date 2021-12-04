import functools

def main():
    file = open("input/3.data", "r")

    # Part 1
    gamma = most_common(file.read().splitlines())
    epsilon = flip_most_common(gamma)

    print("Part 1: "+str(int(gamma, 2) * int(epsilon, 2)))

    file.seek(0)

    # Part 2

    file_list = file.read().splitlines()
    o_gen_rating = reduce_list(gamma, most_common, file_list)
    co2_scrub_rating = reduce_list(epsilon, least_common, file_list)

    print("Part 2: "+str(int(o_gen_rating, 2) * int(co2_scrub_rating, 2)))


def flip_most_common(mc):
    return(bin(int(mc, 2) ^ (2**(len(mc)+1) - 1))[3:])


def least_common(in_list):
    return(flip_most_common(most_common(in_list)))


def most_common(in_list):
    lines = 1
    nums = line_to_list(in_list[0])
    for line in in_list[1:]:
        lines += 1
        nums = list(map(sum, zip(nums, line_to_list(line))))

    return("".join([str(1 if x/lines == 0.5 else round(x/lines)) for x in nums]))


def reduce_list(in_str, common_func, full_list):
    acc_list = full_list
    for i in range(len(in_str)):
        mc = common_func(acc_list)
        acc_list = list(filter(lambda x: x[i] == mc[i], acc_list))
        if len(acc_list) == 1:
            break

    return(acc_list[0])


def line_to_list(line):
    lst = []
    lst[:0] = str(line)
    return list(map(int, lst))


if __name__ == "__main__":
    main()
