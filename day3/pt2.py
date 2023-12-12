file = open("input.txt")

lines = file.readlines()

engine_schematic = [list(line.strip()) for line in lines]

# list of indices we need to check for numbers: up left diagonal, up, up right diagonal, down left diag, down, down right diag, left, right
adjacent_index_checks = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1,], [1, 0], [1, 1]]

def get_gear_ratio(char_index, line_index):
    curr_num = ""
    part_numbers = []
    # loop through each adjacent index check
    for adjacent_index in adjacent_index_checks:
        # try/except in case index is out of bounds
        try:
            # if we find an adjacent digit
            if engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1]].isdigit() == True:
                # current number is this digit
                curr_num = engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1]]
                i = 1
                # find all digits to the left of the orginal digit we found and prepend to current number
                while engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1] - i].isdigit() == True:
                    curr_num = engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1] - i] + curr_num
                    i += 1
                i = 1
                # find all digits to the right of the original digit we found and append to current number
                while engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1] + i].isdigit() == True:
                    curr_num = curr_num + engine_schematic[line_index + adjacent_index[0]][char_index + adjacent_index[1] + i]
                    i += 1
        except:
            # in case we reached end/start of line with a number
            if curr_num != "":
                part_numbers.append(curr_num)
                curr_num = ""
            continue
        # to avoid adding the same number twice in the pair of part numbers
        if curr_num in part_numbers:
            curr_num = ""
        # if we found a new current number append to the part numbers list
        elif curr_num != "":
            part_numbers.append(curr_num)
            curr_num = ""
    # if 2 and only 2 adjacent part numbers were found return gear ratio
    if len(part_numbers) == 2:
        return int(part_numbers[0]) * int(part_numbers[1])
    return 0

total_sum = 0

line_index = 0

for inner_list in engine_schematic:
    char_index = 0
    for char in inner_list:
        if char == "*":
            gear_ratio = get_gear_ratio(char_index, line_index)
            # add to running sum of gear ratios
            total_sum += gear_ratio
        char_index += 1
    line_index += 1

print(total_sum)
