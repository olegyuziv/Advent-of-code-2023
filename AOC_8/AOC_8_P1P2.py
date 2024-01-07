from itertools import cycle
from math import lcm

LEFT, RIGHT = 0, 1  # Constants for directions


def read_file(filename):
    """
    Reads the input file and returns its content as a list of sections.

    :param filename: The name of the file to read.
    :return: A list containing the different sections of the file.
    """
    with open(filename, 'r') as file:
        data = file.read().strip().split('\n\n')
    return data


def process_instructions(raw_instructions):
    """
    Processes raw instructions and converts them to a list of direction constants.

    :param raw_instructions: String of raw instructions.
    :return: A list of direction constants (LEFT or RIGHT).
    """
    return [LEFT if direction == 'L' else RIGHT for direction in raw_instructions]


def process_nodes(raw_nodes):
    """
    Processes raw nodes and creates a mapping from each node to its adjacent nodes.

    :param raw_nodes: String of raw node connections.
    :return: Dictionary mapping each node to a tuple of its adjacent nodes.
    """
    return {line[:3]: (line[7:10], line[12:15]) for line in raw_nodes.splitlines()}


def traverse(node, directions, network):
    """
    Generator function to traverse through the network based on directions.

    :param node: The starting node.
    :param directions: The list of directions to follow.
    :param network: The network of nodes.
    """
    for direction in cycle(directions):
        yield node
        node = network[node][direction]


def task_1(directions, network):
    """
    Solves Task 1 by finding the number of steps to reach 'ZZZ' from 'AAA'.

    :param directions: The list of directions to follow.
    :param network: The network of nodes.
    :return: The number of steps to reach 'ZZZ' from 'AAA'.
    """
    return next(step for step, position in enumerate(traverse('AAA', directions, network)) if position == 'ZZZ')


def task_2(directions, network):
    """
    Solves Task 2 by calculating the least common multiple of steps needed to reach nodes ending with 'Z' from nodes ending with 'A'.

    :param directions: The list of directions to follow.
    :param network: The network of nodes.
    :return: The least common multiple of the required steps.
    """
    steps = [next(step for step, position in enumerate(traverse(start, directions, network)) if position.endswith('Z'))
             for start in (key for key in network if key.endswith('A'))]
    return lcm(*steps)


if __name__ == '__main__':
    raw_instructions, raw_nodes = read_file('puzzle_input')
    instructions = process_instructions(raw_instructions)
    nodes = process_nodes(raw_nodes)

    print(f'Part 1: {task_1(instructions, nodes)}')
    print(f'Part 2: {task_2(instructions, nodes)}')
