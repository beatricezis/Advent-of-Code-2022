def day1():
    max_total_calories = 0
    curr_list = []
    all_calories_list = []

    with open("input_day1", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line == '\n':
            curr_list_sum = sum(curr_list)
            all_calories_list.append(curr_list_sum)
            curr_list.clear()
            if curr_list_sum > max_total_calories:
                max_total_calories = curr_list_sum
        else:
            curr_calories = int(line)
            curr_list.append(curr_calories)

    all_calories_list.sort(reverse=True)
    three_most_calories_list = all_calories_list[:3]

    print("The elf with the most calories is carrying: " + str(max_total_calories))
    print("Total calories of 3 elves that carry the most: " + str(sum(three_most_calories_list)))

    # HOLYCRAP!!
    # "is" keyword is used to check whether the two are the same object.
    # Use "==" instead, to test if two variables are equal.


if __name__ == "__main__":
    day1()
