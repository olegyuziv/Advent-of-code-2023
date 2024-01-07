
# --- Day 2: Cube Conundrum ---
# PART 2

import re

# Limits for each color
color_limits = {'blue': 14, 'green': 13, 'red': 12}


def find_max_for_each_color(attempts):
    """
    Finds the maximum number for each color in a given list of attempts.

    :param attempts: A list of attempt strings, each in the format "number color".
    :return: A dictionary with colors as keys and their maximum numbers as values.
    """
    max_values = {color: 0 for color in color_limits.keys()}

    for attempt in attempts:
        for color_attempt in attempt.split(','):
            number, color = color_attempt.split()
            number = int(number)
            if color in max_values and number > max_values[color]:
                max_values[color] = number

    return max_values


def calculate_line_product(line):
    """
    Calculates the product of the maximum values for each color from a given line.

    :param line: A string representing a line from the file.
    :return: The product of the maximum values.
    """
    _, attempts_str = line.split(':')
    attempts = attempts_str.split(';')
    max_values = find_max_for_each_color(attempts)

    # Calculate the product, using the max value if found, or 1 otherwise
    product = 1
    for color, max_val in max_values.items():
        product *= max_val if max_val > 0 else 1

    return product


def sum_product_of_lines(file_path):
    """
    Sums up the product of maximum values for each line in a file.

    :param file_path: Path to the file containing lines to process.
    :return: The sum of the products for each line.
    """
    total_product_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            total_product_sum += calculate_line_product(line.strip())

    return total_product_sum


# Main execution block
if __name__ == '__main__':
    input_file = "puzzle_input"
    total_product = sum_product_of_lines(input_file)
    print(f"Sum of products for all lines: {total_product}")
