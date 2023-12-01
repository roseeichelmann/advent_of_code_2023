file = open("input.txt")

total_sum = 0

for line in file:
    digits = []
    for char in line:
        if char.isdigit():
            digits.append(char)
    total_sum += int(digits[0] + digits[-1])

print(total_sum)
