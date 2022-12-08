def convert(string):
    list1 = []
    list1[:0] = string
    return list1


def day6():
    num_removed_chars = 0
    with open("input_day6", "r") as file:
        message = file.read()
        while True:
            curr_marker = message[0:14]
            curr_marker = convert(curr_marker)
            if len(curr_marker) <= len(set(curr_marker)):
                break
            else:
                message = message[1:len(message)]
                num_removed_chars = num_removed_chars + 1

        print("The marker was found at the: " + str(num_removed_chars + 14) + "th element")


if __name__ == "__main__":
    day6()
