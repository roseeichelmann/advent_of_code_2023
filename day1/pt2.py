def find_digit(line, word_numbers, is_reversed):
    word = ""
    for char in line:
        if char.isdigit():
            return char
        word += char
        for key in word_numbers:
            # reverse the key if we are using the reversed line
            if (key[::-1] if is_reversed == True else key) in word:
                return word_numbers[key]

file = open("input.txt")

word_numbers = {"one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

total_sum = 0

for line in file:
    # find first digit in the line
    first_digit = find_digit(line, word_numbers, False)
    # once that is done reverse the line and find the last digit
    last_digit = find_digit(line[::-1], word_numbers, True)
    total_sum += int(first_digit + last_digit)

print(total_sum)
