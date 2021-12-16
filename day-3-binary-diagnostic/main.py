import os
import string
import re


def count_bits(values: [string]):
    bits = [0] * len(values[0])
    for value in values:
        for index, bit in enumerate(value):
            bits[index] += int(bit)

    return bits


def get_gamma_epsilon_rates_bits(values: [string]):
    bits = count_bits(values)
    gamma_rate_bits = ['0'] * len(values[0])
    epsilon_rate_bits = ['0'] * len(values[0])

    for index, bit in enumerate(bits):
        if bit >= len(values) / 2:
            gamma_rate_bits[index] = '1'
        else:
            epsilon_rate_bits[index] = '1'

    return gamma_rate_bits, epsilon_rate_bits


def part_1(values: [string]):
    (gamma_rate_bits, epsilon_rate_bits) = get_gamma_epsilon_rates_bits(values)

    gamma_rate = ''.join(gamma_rate_bits)
    epsilon_rate = ''.join(epsilon_rate_bits)

    return int(gamma_rate, 2), int(epsilon_rate, 2), int(gamma_rate, 2) * int(epsilon_rate, 2)


def part_2(values: [string]):
    oxygen_generator_rating = values
    co2_scrubber_rating = values

    oxygen_iteration = 1
    while 1 != len(oxygen_generator_rating):
        oxygen_generator_rating = oxygen_generator(oxygen_generator_rating, oxygen_iteration)
        oxygen_iteration += 1
    oxygen_generator_rate = oxygen_generator_rating[0]

    co2_iteration = 1
    while 1 != len(co2_scrubber_rating):
        co2_scrubber_rating = co2_generator(co2_scrubber_rating, co2_iteration)
        co2_iteration += 1
    co2_scrubber_rate = co2_scrubber_rating[0]

    return int(oxygen_generator_rate, 2), int(co2_scrubber_rate, 2), int(oxygen_generator_rate, 2) * int(co2_scrubber_rate, 2)


def oxygen_generator(values: [string], iteration):
    bits = count_bits(values)
    (gamma_rate_bits, epsilon_rate_bits) = get_gamma_epsilon_rates_bits(values)
    result = []

    pattern = ''
    for index in range(iteration):
        pattern += gamma_rate_bits[index]

    for value in values:
        if re.match(pattern, value):
            result.append(value)

    return result


def co2_generator(values: [string], iteration):
    (gamma_rate_bits, epsilon_rate_bits) = get_gamma_epsilon_rates_bits(values)
    result = []

    pattern = ''
    for index in range(iteration):
        if index < iteration - 1:
            pattern += gamma_rate_bits[index]
        else:
            pattern += epsilon_rate_bits[index]

    for value in values:
        if re.match(pattern, value):
            result.append(value)

    return result


script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    measures = [measure.rstrip("\n") for measure in inputFile.readlines()]

inputFile.close()

print(part_1(measures))
print(part_2(measures))
