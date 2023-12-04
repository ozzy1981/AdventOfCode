def find_calibration_value(line):
    # Extracting the first and last digits from the line
    first_digit = next((char for char in line if char.isdigit()), '0')
    last_digit = next((char for char in reversed(line) if char.isdigit()), '0')
    # Combining them into a two-digit number
    return int(first_digit + last_digit)

file_path = 'input.txt'

sum_of_values = 0
with open(file_path, 'r') as file:
    for line in file:
        sum_of_values += find_calibration_value(line.strip())

print(sum_of_values)
