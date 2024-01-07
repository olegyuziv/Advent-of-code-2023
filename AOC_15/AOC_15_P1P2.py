from functools import reduce


def read_first_line_from_file(file_name):
    """
    Reads and returns the first line from the given file.

    :param file_name: Path to the file to be read.
    :return: The first line of the file as a string.
    """
    with open(file_name, 'r') as f:
        return f.readline().strip()


def split_line_into_sequences(line):
    """
    Splits a line into sequences separated by commas.

    :param line: A string representing a line from the file.
    :return: List of sequences.
    """
    return line.split(',')


def calculate_hash(sequence):
    """
    Calculates a custom hash value for a given sequence.

    :param sequence: The sequence for which the hash is to be calculated.
    :return: Hash value for the sequence.
    """
    return reduce(lambda v, ch: (v + ord(ch)) * 17 % 256, sequence, 0)


def sum_of_hashes(sequences):
    """
    Calculates the sum of hash values for each sequence in the list.

    :param sequences: List of sequences to be hashed.
    :return: Sum of hash values.
    """
    return sum(calculate_hash(sequence) for sequence in sequences)


def calculate_power(sequences):
    """
    Calculates the power based on the given sequences.

    :param sequences: List of sequences representing box names and values.
    :return: Total power calculated from the box values.
    """
    boxes = [{} for _ in range(256)]

    for sequence in sequences:
        handle_sequence(sequence, boxes)

    return calculate_total_power(boxes)


def handle_sequence(sequence, boxes):
    """
    Handles a single sequence and updates boxes accordingly.

    :param sequence: A sequence from the list.
    :param boxes: List of dictionaries representing the boxes.
    """
    if sequence.endswith('-'):
        remove_from_box(sequence, boxes)
    else:
        add_to_box(sequence, boxes)


def remove_from_box(sequence, boxes):
    """
    Removes a name from the corresponding box based on the sequence.

    :param sequence: A sequence indicating a name to be removed.
    :param boxes: List of dictionaries representing the boxes.
    """
    name = sequence[:-1]
    boxes[calculate_hash(name)].pop(name, None)


def add_to_box(sequence, boxes):
    """
    Adds a value to a box based on the sequence.

    :param sequence: A sequence indicating a name and value to be added.
    :param boxes: List of dictionaries representing the boxes.
    """
    name, value = sequence.split('=')
    boxes[calculate_hash(name)][name] = int(value)


def calculate_total_power(boxes):
    """
    Calculates the total power based on the box values.

    :param boxes: List of dictionaries representing the boxes.
    :return: Total power.
    """
    power = 0
    for bid, box in enumerate(boxes, start=1):
        power += sum(bid * sid * value for sid, value in enumerate(box.values(), start=1))
    return power


if __name__ == '__main__':
    line = read_first_line_from_file('puzzle_input')
    sequences = split_line_into_sequences(line)

    print(f'Part 1: {sum_of_hashes(sequences)}')
    print(f'Part 2: {calculate_power(sequences)}')
