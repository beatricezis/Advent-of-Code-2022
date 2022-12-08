def common_range(a, b):
    list_one = set(a)
    list_two = set(b)
    return True if list_one & list_two else False


def day4():
    first_worker_sections = []
    second_worker_sections = []
    pairs_that_fully_contain_the_other = 0
    overlap_ranges = 0

    with open("input_day4", "r") as file:
        lines = file.readlines()
        for line in lines:
            A = line.split(',')[0]
            from1 = int(A.split('-')[0])
            to1 = int(A.split('-')[1]) + 1
            for x in range(from1, to1):
                first_worker_sections.append(x)

            B = (line.split(',')[1])[:-1]
            from2 = int(B.split('-')[0])
            to2 = int(B.split('-')[1]) + 1
            for x in range(from2, to2):
                second_worker_sections.append(x)

            intersect = all(item in first_worker_sections for item in second_worker_sections) or \
                all(item in second_worker_sections for item in first_worker_sections)

            if intersect:
                pairs_that_fully_contain_the_other = pairs_that_fully_contain_the_other + 1

            overlap = common_range(first_worker_sections, second_worker_sections)
            if overlap:
                overlap_ranges = overlap_ranges + 1

            first_worker_sections.clear()
            second_worker_sections.clear()

        print("Number of sections that contain others: " + str(pairs_that_fully_contain_the_other))
        print("Number of overlap ranges is: " + str(overlap_ranges))


if __name__ == "__main__":
    day4()
