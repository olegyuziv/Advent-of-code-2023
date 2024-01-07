

# --- Day 6: Wait For It ---

import math

def read_file(file_name: str) -> str:
    """Reads the entire content from the specified file."""
    with open(file_name, 'r') as file:
        return file.read().strip()


def parse_times_and_distances(data_str: str, fix_kerning: bool) -> list:
    """
    Parses times and distances from the given string.

    :param data_str: String containing the raw data.
    :param fix_kerning: Flag to indicate whether to fix kerning or not.
    :return: List of tuples containing times and distances.
    """
    times_str, distances_str = data_str.splitlines()
    times_str = times_str.split(':')[1].strip()
    distances_str = distances_str.split(':')[1].strip()

    if fix_kerning:
        times_str = times_str.replace(' ', '')
        distances_str = distances_str.replace(' ', '')
        return [(int(times_str), int(distances_str))]

    times = [int(n) for n in times_str.split()]
    distances = [int(n) for n in distances_str.split()]
    return list(zip(times, distances))


def calculate_options_for_race(record: int, distance: int) -> int:
    """
    Calculates the number of options for a single race.

    :param record: Record time for the race.
    :param distance: Distance for the race.
    :return: Number of options where the record can be beaten.
    """
    return sum(1 for delay in range(1, distance) if distance / delay + delay < record)


def solve_task_1(races: list) -> int:
    """
    Solves the first task by calculating the product of the number of options for each race.
    """
    return math.prod([calculate_options_for_race(record, distance) for record, distance in races])


def solve_task_2(race: tuple) -> int:
    """
    Solves the second task by finding the difference between two possible delay values.
    """
    record, distance = race
    x1 = (record - math.sqrt(record ** 2 - 4 * distance)) // 2
    x2 = (record + math.sqrt(record ** 2 - 4 * distance)) // 2
    return int(abs(x1 - x2))


def main():
    """Main function to execute tasks."""
    file_content = read_file('puzzle_input')
    races = parse_times_and_distances(file_content, False)
    race = parse_times_and_distances(file_content, True)[0]

    print(f'Part 1: {solve_task_1(races)}')
    print(f'Part 2: {solve_task_2(race)}')


if __name__ == '__main__':
    main()
