
# --- Day 3: Gear Ratios ---
# PART 2

def read_engine_map(file_path):
    """
    Reads the engine map from a file.

    :param file_path: Path to the file.
    :return: List of strings, each representing a row of the engine map.
    """
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def get_neighbors(coord_x, coord_y):
    """
    Generates neighboring coordinates around a given point.

    :param coord_x: X-coordinate of the central point.
    :param coord_y: Y-coordinate of the central point.
    :return: Generator for neighboring coordinates.
    """
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx != 0 or dy != 0:
                yield coord_x + dx, coord_y + dy

def find_horizontal_numbers(x, y, direction, engine_map):
    """
    Recursively finds a number in a horizontal direction from a starting point.

    :param x: Starting X-coordinate.
    :param y: Starting Y-coordinate.
    :param direction: Direction for horizontal search (1 for right, -1 for left).
    :param engine_map: The engine map data.
    :return: Number found in the specified direction.
    """
    if 0 <= x < len(engine_map[0]) and engine_map[y][x].isdigit():
        return engine_map[y][x] + find_horizontal_numbers(x + direction, y, direction, engine_map)
    return ''

def get_numbers_around_star(x, y, engine_map):
    """
    Gets numbers surrounding a star in the engine map.

    :param x: X-coordinate of the star.
    :param y: Y-coordinate of the star.
    :param engine_map: The engine map data.
    :return: List of numbers found around the star.
    """
    numbers = set()
    for nx, ny in get_neighbors(x, y):
        if 0 <= ny < len(engine_map) and 0 <= nx < len(engine_map[0]):
            left_number = find_horizontal_numbers(nx - 1, ny, -1, engine_map)
            right_number = find_horizontal_numbers(nx + 1, ny, 1, engine_map)
            full_number = left_number[::-1] + engine_map[ny][nx] + right_number
            if full_number.isdigit():
                numbers.add(int(full_number))
    return numbers

def calculate_total_sum(engine_map):
    """
    Calculates the total sum based on the engine map criteria.

    :param engine_map: The engine map data.
    :return: Total sum calculated from the engine map.
    """
    total = 0
    for y, row in enumerate(engine_map):
        for x, char in enumerate(row):
            if char == '*':
                surrounding_numbers = get_numbers_around_star(x, y, engine_map)
                if len(surrounding_numbers) == 2:
                    total += surrounding_numbers.pop() * surrounding_numbers.pop()
    return total

# Main execution
if __name__ == '__main__':
    engine_map_data = read_engine_map('puzzle_input')
    total_sum = calculate_total_sum(engine_map_data)
    print(f"Total Sum: {total_sum}")
