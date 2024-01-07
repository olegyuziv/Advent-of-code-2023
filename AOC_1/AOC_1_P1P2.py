
# --- Day 1: Trebuchet?! ---

# Dictionary mapping word representations of numbers to their numeric values
num_words_to_digits = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9,
}


def convert_line_to_numbers(line, enable_word_conversion):
    """
    Converts a line of text to a list of numbers. This function looks for digits
    and word representations of numbers in the text, converting them to integers.

    :param line: A string containing the text to be processed.
    :param enable_word_conversion: A boolean that enables conversion of words to numbers.
    :return: A list of integers found in the line.
    """
    numbers = []
    word = ''

    for char in line:
        if char.isdigit():
            # Add the digit to the numbers list
            numbers.append(int(char))
        elif char.isalpha():
            # Build the word, and if it forms a valid number word, convert it
            word += char
            if word in num_words_to_digits and enable_word_conversion:
                numbers.append(num_words_to_digits[word])
                word = ''  # Reset word for next potential number word

    return numbers


def read_file_and_convert(file_path, convert_words=False):
    """
    Reads a file line by line and converts each line to a list of numbers
    based on the convert_line_to_numbers function.

    :param file_path: Path of the file to read.
    :param convert_words: Whether to convert number words to digits.
    :return: A list of tuples, each containing the first and last number from each line.
    """
    result = []

    with open(file_path, 'r') as file:
        for line in file:
            # Convert each line to a list of numbers
            num_list = convert_line_to_numbers(line, convert_words)
            # Append a tuple of the first and last number in the list, if available
            if num_list:
                result.append((num_list[0], num_list[-1]))

    return result


def compute_sum(data_list):
    """
    Computes the sum of first and last numbers multiplied by 10 for each tuple in the data list.

    :param data_list: List of tuples, where each tuple contains two integers.
    :return: Computed sum as per the defined formula.
    """
    # Sum up the first number multiplied by 10 plus the last number for each tuple
    return sum(first * 10 + last for first, last in data_list)


# Main function
if __name__ == '__main__':
    # Process the file without and with converting word representations
    input_data_basic = read_file_and_convert('puzzle_input')
    input_data_advanced = read_file_and_convert('puzzle_input', True)

    # Print the results of the computations
    print(f'Part 1: {compute_sum(input_data_basic)}')
    print(f'Part 2: {compute_sum(input_data_advanced)}')
