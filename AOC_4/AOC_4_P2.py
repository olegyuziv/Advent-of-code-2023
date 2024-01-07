
# --- Day 4: Scratchcards ---
# PART 2

def read_and_parse_cards(file_path):
    """
    Reads and parses card data from a file.

    :param file_path: Path to the file.
    :return: List of tuples, each containing winning numbers and given numbers for each line.
    """
    with open(file_path, 'r') as file:
        return [parse_line(line.strip()) for line in file]

def parse_line(line):
    """
    Parses a single line to extract winning numbers and numbers given.

    :param line: A string representing a line from the file.
    :return: A tuple of two elements - a set of winning numbers and a list of given numbers.
    """
    parts = line.split(":")
    winning = set(parts[1].split("|")[0].strip().split())
    given = parts[1].split("|")[1].strip().split()
    return winning, given

def calculate_total_wins(card_data):
    """
    Calculates the total number of wins from the card data.

    :param card_data: List of tuples containing winning numbers and given numbers for each card.
    :return: Total number of wins calculated from all cards.
    """
    total_wins = 0
    memo = {}
    card_points = {idx: sum(1 for num in given if num in winning) for idx, (winning, given) in enumerate(card_data)}

    for card in card_points:
        total_wins += count_wins_recursive(card_points, card, memo)

    return total_wins

def count_wins_recursive(points, current_card, memo):
    """
    Recursively counts the number of wins using memoization.

    :param points: Dictionary of points for each card.
    :param current_card: Current card index.
    :param memo: Dictionary for memoization.
    :return: Count of wins for the current card.
    """
    if current_card not in points:
        return 0

    if current_card in memo:
        return memo[current_card]

    total = 1  # Base count for the current card
    next_card_limit = current_card + points[current_card]

    for next_card in range(current_card + 1, next_card_limit + 1):
        total += count_wins_recursive(points, next_card, memo)

    memo[current_card] = total
    return total

# Main execution block
if __name__ == '__main__':
    card_lines = read_and_parse_cards("puzzle_input")
    total_wins = calculate_total_wins(card_lines)
    print(f"Total Wins: {total_wins}")
