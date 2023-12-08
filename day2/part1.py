file = open("input.txt")

num_cubes_in_bag = {"red": 12, "green": 13, "blue": 14}

sum_of_ids = 0

def determine_if_game_possible(game_id, sets):
    # Loop thru each set in the game
    for set in sets:
        set_colors = set.strip().split(",")
        # Loop thru each color in the set
        for set_color in set_colors:
            number = int(set_color.strip().split(" ")[0])
            color = set_color.strip().split(" ")[1]
            # If more cubes of this color were pulled out than are actually in the bag
            # return 0, this was not a possible game
            if number > num_cubes_in_bag[color]:
                return 0;
    return game_id

for line in file:
    split_line = line.strip("\n").split(":")
    game_id = int(split_line[0].split("Game ")[1])
    sets = split_line[1].split(";")
    sum_of_ids += determine_if_game_possible(game_id, sets)

print(sum_of_ids, "This is the sum of possible game ids")