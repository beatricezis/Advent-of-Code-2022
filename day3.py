def day3():
    diff_lowercase = 96
    diff_uppercase = 38
    priority_sum = 0

    with open("input_day3", "r") as file:
        lines = file.readlines()
    for line in lines:
        first_part = line[:len(line) // 2]
        second_part = line[len(line) // 2:]
        common_type = ''.join(set(first_part).intersection(second_part))
        if common_type.isupper():
            curr_priority = ord(common_type) - diff_uppercase
        else:
            curr_priority = ord(common_type) - diff_lowercase

        priority_sum = priority_sum + curr_priority

    print("Sum of priorities is: " + str(priority_sum))


def day3_part2():
    diff_lowercase = 96
    diff_uppercase = 38
    priority_sum = 0
    team = []

    with open("input_day3", "r") as file:
        lines = file.readlines()
    for line in lines:
        team.append(line)
        if len(team) == 3:
            common_type1 = ''.join(set(team[0][:-1]).intersection(team[1][:-1]))
            common_type2 = ''.join(set(team[1][:-1]).intersection(team[2][:-1]))
            common_type3 = ''.join(set(common_type1).intersection(common_type2))

            if common_type3.isupper():
                curr_priority = ord(common_type3) - diff_uppercase
            else:
                curr_priority = ord(common_type3) - diff_lowercase

            priority_sum = priority_sum + curr_priority
            team.clear()

    print("Sum of priorities is: " + str(priority_sum))


if __name__ == "__main__":
    day3_part2()
