from pprint import pprint
sample = []

with open('input3.txt', 'r') as f:
    sample = f.readlines()

for i in range(len(sample)):
    sample[i] = sample[i].strip('\n')

groups = []
for i in range(0, len(sample), 3):
    group = []
    group.append(sample[i])
    group.append(sample[i+1])
    group.append(sample[i+2])
    groups.append(group)
    pass

letters = {}
for i in range(97, 97+26):
    letters[chr(i)] = i - 96
for i in range(65, 65 + 26):
    letters[chr(i)] = i - 65 + 27

total_priority = 0
for group in groups:
    for l in group[0]:
        if l in group[1]:
            if l in group[2]:
                total_priority += letters[l]
                break
print(total_priority)
