
# --- Day 3: Gear Ratios ---
# PART 1

def get_surrounding_cells(x, y):
    """
    Generates the coordinates of surrounding cells in a grid around (x, y).

    :param x: X-coordinate of the center cell.
    :param y: Y-coordinate of the center cell.
    :return: Generator for coordinates of surrounding cells.
    """
    # List of relative positions around the cell
    neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for dx, dy in neighbor_offsets:
        yield x + dx, y + dy


def read_engine_map(file_path):
    """
    Reads the engine map from a file.

    :param file_path: Path to the file containing the engine map.
    :return: List of strings, each representing a row of the engine map.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


def create_validity_map(engine_map):
    """
    Creates a map indicating valid part numbers in the engine map.

    :param engine_map: The engine map as a list of strings.
    :return: 2D list indicating valid parts (1 for valid, 0 for invalid).
    """
    validity_map = [[0] * len(engine_map[0]) for _ in engine_map]
    for y, row in enumerate(engine_map):
        for x, char in enumerate(row):
            if char not in ".0123456789":
                for nx, ny in get_surrounding_cells(x, y):
                    if 0 <= nx < len(row) and 0 <= ny < len(engine_map):
                        validity_map[ny][nx] = 1
    return validity_map


def sum_valid_parts(engine_map, validity_map):
    """
    Sums the part numbers in the engine map that are marked as valid.

    :param engine_map: The engine map as a list of strings.
    :param validity_map: 2D list indicating valid parts.
    :return: Sum of valid part numbers.
    """
    sum_parts, current_number, is_valid = 0, '', False
    for y, row in enumerate(engine_map):
        for x, char in enumerate(row):
            if char.isdigit():
                current_number += char
                is_valid |= validity_map[y][x]
            else:
                if is_valid and current_number:
                    sum_parts += int(current_number)
                current_number, is_valid = '', False

    return sum_parts + int(current_number) if is_valid and current_number else sum_parts


# Main execution block
if __name__ == '__main__':
    engine_map = read_engine_map('puzzle_input')
    validity_map = create_validity_map(engine_map)
    total_sum = sum_valid_parts(engine_map, validity_map)
    print(f"Total Sum of Valid Parts: {total_sum}")

