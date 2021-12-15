import os
script_dir = os.path.dirname(__file__)
rel_path = "input.txt"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path) as inputFile:
    measures = [int(measure) for measure in inputFile.readlines()]

previous = measures[0]
increments = 0

for measure in measures:
    print(measure, previous, measure > previous)
    if measure > previous:
        increments += 1

    previous = measure

print increments

inputFile.close()
