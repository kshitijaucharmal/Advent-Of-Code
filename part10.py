from pprint import pprint

crates = [
['W', 'B', 'G', 'Z', 'R', 'D', 'C', 'V'],
['V', 'T', 'S', 'B', 'C', 'F', 'W', 'G'],
['W', 'N', 'S', 'B', 'C'],
['P', 'C', 'V', 'J', 'N', 'M', 'G', 'Q'],
['B', 'H', 'D', 'F', 'L', 'S', 'T'],
['N', 'M', 'W', 'T', 'V', 'J'],
['G', 'T', 'S', 'C', 'L', 'F', 'P'],
['Z', 'D', 'B'],
['W', 'Z', 'N', 'M'],
]

# reverse crates order
for i in range(len(crates)):
    crates[i].reverse()

with open('instructions.txt', 'r') as f:
    instructions = f.readlines()

# cleaning instructions
for i in range(len(instructions)):
    instructions[i] = [int(a) for a in instructions[i].strip('\n').split('-')]

for order in instructions:
    n_boxes = order[0]
    move_from = order[1] - 1 # -1 cause it starts from 1
    move_to = order[2] - 1 # same

    boxes = crates[move_from][-n_boxes:]
    crates[move_from] = crates[move_from][:-n_boxes]
    crates[move_to] += boxes

s = ""
for c in crates:
    s += c[-1]

pprint(s)
