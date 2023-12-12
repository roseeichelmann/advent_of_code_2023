file = open("input.txt")

lines = file.readlines()

engine_schematic = [list(line.strip()) for line in lines]

list_index = 0

# list of indices we need to check for symbols: up left diagonal, up, up right diagonal, down left diag, down, down right diag, left, right
adjacent_index_checks = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1,], [1, 0], [1, 1]]

total_sum = 0

def check_if_has_adjacent_symbol(list_index, char_index):
    for adjacent_index in adjacent_index_checks:
        # need to make sure the list index we are about to check is not out of range here
        try:
            engine_schematic[list_index + adjacent_index[0]][char_index + adjacent_index[1]]
        # if it is then skip to trying next index
        except:
            continue
        # if we just found a non alphnum symbol thats not a period then we have an adjacent symbol!!!
        if engine_schematic[list_index + adjacent_index[0]][char_index + adjacent_index[1]].isalnum() == False and engine_schematic[list_index + adjacent_index[0]][char_index + adjacent_index[1]] != ".":
            return True
    return False

for inner_list in engine_schematic:
    char_index = 0
    curr_num = ""
    has_adjacent_symbol = False
    for char in inner_list:
        if char.isdigit():
            curr_num += char
            # if we dont already have an adjacent symbol for current num then check for one
            if has_adjacent_symbol == False:
                has_adjacent_symbol = check_if_has_adjacent_symbol(list_index, char_index)
        # once we get to a char that is not a digit OR at the end of a line
        if char.isdigit() == False or char_index == len(inner_list) - 1:
            # if we havent reset the current number yet then check if we ever found an adjacent symbol for the current num
            if curr_num != "":
                # yay this num had an adjacent symbol lets add it to the running total
                if has_adjacent_symbol == True:
                    total_sum += int(curr_num)
                    has_adjacent_symbol = False
                    curr_num = ""
                curr_num = ""
        char_index += 1
    list_index += 1

print(total_sum, "this is the total sum")
