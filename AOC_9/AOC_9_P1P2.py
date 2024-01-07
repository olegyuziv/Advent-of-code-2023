import itertools

def read_sequences(file_path):
    """
    Reads sequences from a file and converts them to a list of integer lists.

    :param file_path: Path to the file to be read.
    :return: List of integer lists, each list representing a sequence from the file.
    """
    with open(file_path, 'r') as file:
        data = file.readlines()
    return [[int(item) for item in line.strip().split()] for line in data]

def next_sequence(seq):
    """
    Generates the next sequence by subtracting each pair of consecutive numbers.

    :param seq: The current sequence as a list of integers.
    :return: The next sequence obtained by subtracting consecutive pairs.
    """
    return [y - x for x, y in itertools.pairwise(seq)]

def calculate_extrapolation(seq):
    """
    Calculates the extrapolation of a sequence.

    :param seq: The initial sequence as a list of integers.
    :return: The extrapolated result as an integer.
    """
    result = seq[-1]  # Initialize with the last element of the sequence
    while any(num != 0 for num in seq):  # Continue until all elements are zero
        seq = next_sequence(seq)
        result += seq[-1]  # Add the last element of the new sequence
    return result

def pairwise(iterable):
    """
    Custom implementation of itertools.pairwise for Python versions earlier than 3.10.
    Yields successive overlapping pairs taken from the input iterable.

    :param iterable: An iterable from which to produce pairs.
    :return: An iterator of pairs.
    """
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def next_sequence(seq):
    """
    Generates the next sequence by subtracting each pair of consecutive numbers.

    :param seq: The current sequence as a list of integers.
    :return: The next sequence obtained by subtracting consecutive pairs.
    """
    return [y - x for x, y in pairwise(seq)]

def process_sequences(sequences, reverse=False):
    """
    Processes a list of sequences and calculates their total extrapolation.

    :param sequences: List of integer sequences.
    :param reverse: Boolean flag to indicate whether to reverse the sequences.
    :return: Total extrapolation for all sequences.
    """
    total = 0
    for sequence in sequences:
        if reverse:
            sequence = sequence[::-1]  # Reverse the sequence if required
        total += calculate_extrapolation(sequence)
    return total

def main():
    """
    Main function to execute the script.
    """
    sequence_data = read_sequences('puzzle_input')
    print(f'Result for Part 1: {process_sequences(sequence_data)}')
    print(f'Result for Part 2: {process_sequences(sequence_data, reverse=True)}')

if __name__ == "__main__":
    main()
