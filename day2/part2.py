file = open("input.txt")

sum_of_power_of_cubes = 0

def get_sum_of_power_of_cubes(game_id, sets):
    num_cubes_in_game = {"red": 0, "green": 0, "blue": 0}
    # Loop thru each set in the game
    for set in sets:
        set_colors = set.strip().split(",")
        # Loop thru each color in the set
        for set_color in set_colors:
            number = int(set_color.strip().split(" ")[0])
            color = set_color.strip().split(" ")[1]
            # Find the minimum number of cubes for each color
            if number > num_cubes_in_game[color]:
                num_cubes_in_game[color] = number
    power_of_cubes = num_cubes_in_game["red"] * num_cubes_in_game["green"] * num_cubes_in_game["blue"]
    return power_of_cubes

for line in file:
    split_line = line.strip("\n").split(":")
    game_id = int(split_line[0].split("Game ")[1])
    sets = split_line[1].split(";")
    sum_of_power_of_cubes += get_sum_of_power_of_cubes(game_id, sets)

print(sum_of_power_of_cubes, "This is the sum of the power of cubes")