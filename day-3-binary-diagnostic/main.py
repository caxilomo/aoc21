import os
import string


def part_1(values: [string]):
    bits = [0] * len(values[0])
    gamma_rate_bits = ['0'] * len(values[0])
    epsilon_rate_bits = ['0'] * len(values[0])

    for value in values:
        for index, bit in enumerate(value):
            bits[index] += int(bit)

    for index, bit in enumerate(bits):
        if bit > len(values) / 2:
            gamma_rate_bits[index] = '1'
        else:
            epsilon_rate_bits[index] = '1'

    gamma_rate = ''.join(gamma_rate_bits)
    epsilon_rate = ''.join(epsilon_rate_bits)

    return int(gamma_rate, 2), int(epsilon_rate, 2), int(gamma_rate, 2) * int(epsilon_rate, 2)


script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    measures = [measure.rstrip("\n") for measure in inputFile.readlines()]

inputFile.close()

print(part_1(measures))
