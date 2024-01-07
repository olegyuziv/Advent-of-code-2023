
# --- Day 5: If You Give A Seed A Fertilizer ---
# PART 2

from functools import reduce  # Import the 'reduce' function from the 'functools' module

# Open the file 'puzzle_input', read its content, and split it into sections by double newline.
# Assign the first section to 'seeds' and the rest to 'mappings'.
with open('puzzle_input') as file:
    seeds, *mappings = file.read().split('\n\n')

# Converting the seed values from strings to integers, skipping the first item.
seeds = list(map(int, seeds.split()[1:]))

# Define the 'lookup' function to process inputs based on a given mapping.
def lookup(inputs, mapping):
    for start, length in inputs:  # Iterate over each pair of start and length in the inputs.
        while length > 0:  # Continue processing while there is length remaining.
            for m in mapping.split('\n')[1:]:  # Iterate over each line in the mapping, skipping the first line.
                dst, src, len = map(int, m.split())  # Extract destination, source, and length from the mapping line.
                delta = start - src  # Calculate the delta between start and source.
                if 0 <= delta < len:  # Check if delta is within the range of the mapping length.
                    len = min(len - delta, length)  # Calculate the effective length to process.
                    yield (dst + delta, len)  # Yield the new start position and the processed length.
                    start += len  # Update start for next iteration.
                    length -= len  # Update length for next iteration.
                    break  # Break the loop to process the next part of the input.
            else:
                yield (start, length)  # Yield the remaining part of the input if no mapping applies.
                break

# Process the seeds and print the results.
# Pair the seeds, apply the lookup function through all mappings,
# and find the minimum result for each pair.
pairs = zip(seeds[::2], seeds[1::2])  # Creating pairs from the seeds
result = [min(reduce(lookup, mappings, [pair]))[0] for pair in pairs]  # Processing each pair through the mappings
print(*result)

# Putting each result in the Advent of Code result until it works
