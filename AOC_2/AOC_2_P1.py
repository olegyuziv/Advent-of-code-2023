
# --- Day 2: Cube Conundrum ---
# PART 1

import re

# Maximum allowed attempts for each color
color_max_attempts = {'blue': 14, 'green': 13, 'red': 12}

def check_attempts_validity(attempts):
    """
    Checks if all attempts in the given list are valid based on the maximum allowed attempts
    for each color.

    :param attempts: A list of strings, each representing an attempt in the format 'number color'.
    :return: True if all attempts are valid, False otherwise.
    """
    for attempt in attempts:
        # Split each attempt into individual color attempts
        color_attempts = [info.split() for info in attempt.split(',')]
        # Check each color attempt against the maximum allowed attempts
        for number, color in color_attempts:
            if int(number) > color_max_attempts[color]:
                return False
    return True

def extract_game_number(line):
    """
    Extracts the game number from a line if all attempts are valid.

    :param line: A string representing a line from the file.
    :return: The game number if valid, otherwise 0.
    """
    game_id, attempts_str = line.split(':')
    attempts = attempts_str.split(';')
    # Check if all attempts are valid
    if check_attempts_validity(attempts):
        # Find the first number in the game ID
        game_number = re.search(r'\d+', game_id)
        return int(game_number.group()) if game_number else 0
    return 0

def sum_valid_game_numbers(file_path):
    """
    Calculates the sum of all valid game numbers from a file.

    :param file_path: Path to the file containing game information.
    :return: Sum of all valid game numbers.
    """
    total_sum = 0
    with open(file_path, 'r') as file:
        # Iterate through each line in the file
        for line in file:
            total_sum += extract_game_number(line.strip())
    return total_sum

# Main execution block
if __name__ == '__main__':
    input_file = "puzzle_input"
    total_sum_games = sum_valid_game_numbers(input_file)
    print(f"Sum of valid game numbers: {total_sum_games}")
