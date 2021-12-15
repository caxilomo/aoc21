import os
import re
import string
from typing import Tuple


def get_steps(patter, command) -> int:
    steps = re.findall(patter, command)
    if not steps:
        return 0

    return int(steps[0])


def get_forward_steps(command) -> int:
    return get_steps("forward (\d)+", command)


def get_down_steps(command) -> int:
    return get_steps("down (\d)+", command)


def get_up_steps(command) -> int:
    return get_steps("up (\d)+", command)


def part_1(values: [string]) -> Tuple[int, int, int]:
    position = 0
    depth = 0
    for value in values:
        position += get_forward_steps(value)
        depth += get_down_steps(value)
        depth -= get_up_steps(value)


    return position, depth, position * depth


def part_2(values: [string]) -> Tuple[int, int, int]:
    position = 0
    depth = 0
    aim = 0

    for value in values:
        position += get_forward_steps(value)
        depth += aim * get_forward_steps(value)
        aim += get_down_steps(value)
        aim -= get_up_steps(value)

    return position, depth, position * depth


script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    commands = [command for command in inputFile.readlines()]

inputFile.close()

print(part_1(commands))
print(part_2(commands))
