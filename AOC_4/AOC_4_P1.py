
# --- Day 4: Scratchcards ---
# PART 1

def read_card_data(file_path):
    """
    Reads card data from a file.

    :param file_path: Path to the file.
    :return: List of tuples containing winning and given numbers for each line.
    """
    with open(file_path, 'r') as file:
        return [parse_line_data(line.strip()) for line in file]

def parse_line_data(line):
    """
    Parses a line of the file to extract winning and given numbers.

    :param line: A string representing a line from the file.
    :return: A tuple containing sets of winning numbers and given numbers.
    """
    parts = line.split(":")
    winning_numbers = set(parts[1].split("|")[0].split())
    numbers_given = parts[1].split("|")[1].split()
    return winning_numbers, numbers_given

def compute_points_for_line(winning_numbers, numbers_given):
    """
    Computes the points for a line based on the winning and given numbers.

    :param winning_numbers: Set of winning numbers.
    :param numbers_given: List of given numbers.
    :return: Points earned for the line.
    """
    points = 0
    for num in numbers_given:
        if num in winning_numbers:
            points = 1 if points == 0 else points * 2
    return points

def calculate_total_points(card_data):
    """
    Calculates the total points based on all lines of card data.

    :param card_data: List of tuples containing winning and given numbers.
    :return: Total points calculated.
    """
    return sum(compute_points_for_line(winning, given) for winning, given in card_data)

# Main execution block
if __name__ == '__main__':
    file_path = "puzzle_input"
    card_data = read_card_data(file_path)
    total_points = calculate_total_points(card_data)
    print(f"Total Points: {total_points}")
