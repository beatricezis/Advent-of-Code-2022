def day5():
    list_of_stacks = []
    initialization_done = False
    string = ""
    bunch_of_boxes_to_move = []

    with open("input_day5", "r") as file:
        lines = file.readlines()
        for line in lines:
            if line != '\n' and not initialization_done:
                line = line.replace('\n', '')
                stack = line.split(' ')
                list_of_stacks.append(stack)
                continue
            if line == '\n':
                initialization_done = True
                continue
            line = line.replace('\n', '')
            curr_operation = line.split(' ')
            _move = int(curr_operation[1])
            _from = int(curr_operation[3]) - 1
            _to = int(curr_operation[5]) - 1

            for x in range(_move):
                element = list_of_stacks[_from].pop()
                bunch_of_boxes_to_move.append(element)
            for x in range(_move):
                list_of_stacks[_to].append(bunch_of_boxes_to_move.pop())

            bunch_of_boxes_to_move.clear()

        for stack in list_of_stacks:
            string = string + stack[-1]

        print("The string is: " + string)


if __name__ == "__main__":
    day5()
