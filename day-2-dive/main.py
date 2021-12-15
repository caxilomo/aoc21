import os
import re


def get_steps(patter, command) -> int:
    forward_steps = re.findall(patter, command)
    if not forward_steps:
        return 0

    return int(forward_steps[0])


def get_forward_steps(command) -> int:
    return get_steps("forward (\d)+", command)


def get_down_steps(command) -> int:
    return get_steps("down (\d)+", command)


def get_up_steps(command) -> int:
    return get_steps("up (\d)+", command)


script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    commands = [command for command in inputFile.readlines()]

inputFile.close()

position = 0
depth = 0

for command in commands:
    position += get_forward_steps(command)
    depth += get_down_steps(command)
    depth -= get_up_steps(command)

print(position, depth, position * depth)
