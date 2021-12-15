import os


def part_1(values: [int]) -> int:
    previous = values[0]
    increments = 0

    for measure in values:
        if measure > previous:
            increments += 1

        previous = measure

    return increments


def part_2(values: [int]) -> int:
    current_window = values[0] + values[1] + values[2]
    increments = 0
    window_size = 3
    windows = (len(values) - len(values) % window_size) - 1

    for window in range(windows):
        next_window = values[window + 1] + values[window + 2] + values[window + 3]

        if next_window > current_window:
            increments += 1

        current_window = next_window

    return increments


script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    measures = [int(measure) for measure in inputFile.readlines()]

inputFile.close()

print(part_1(measures))
print(part_2(measures))
