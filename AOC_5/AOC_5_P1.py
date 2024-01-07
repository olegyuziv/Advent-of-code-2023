
# --- Day 5: If You Give A Seed A Fertilizer ---
# PART 1

def read_file_data(file_path):
    """
    Reads the file data and separates the seeds and maps.

    :param file_path: Path to the file.
    :return: Tuple containing seeds and list of maps.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    seeds, *maps = content.split('\n\n')
    return seeds, maps

def process_maps(val, map_list):
    """
    Processes a value through a series of maps.

    :param val: Initial value to process.
    :param map_list: List of maps to apply to the value.
    :return: Processed value after applying all maps.
    """
    for m in map_list:
        val = map_value(val, m)
    return val

def map_value(val, m):
    """
    Maps a value using a single map.

    :param val: Value to map.
    :param m: Map to use for mapping the value.
    :return: Mapped value.
    """
    _, *lines = m.split('\n')
    for line in lines:
        dst, src, n = map(int, line.split())
        if src <= val < src + n:
            return val - src + dst
    return val

def find_minimum_mapped_value(filename):
    """
    Finds the minimum mapped value from seeds and maps in the file.

    :param filename: Name of the file containing seeds and maps.
    :return: Minimum mapped value.
    """
    seeds, maps = read_file_data(filename)
    seed_values = map(int, seeds.split()[1:])
    mapped_values = [process_maps(seed, maps) for seed in seed_values]
    return min(mapped_values)

# Main execution block
if __name__ == '__main__':
    result = find_minimum_mapped_value('puzzle_input')
    print(f"Minimum Mapped Value: {result}")
