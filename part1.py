inputs = []
with open('input.txt', 'r') as f:
    inputs = f.readlines()

for i in range(len(inputs)):
    inputs[i] = inputs[i].strip('\n')
    if inputs[i] != '':
        inputs[i] = int(inputs[i])

max_cals = 0 
total = 0

for i in range(len(inputs)):
    if (inputs[i] == ''):
        if total > max_cals:
            max_cals = total
        total = 0
        continue
    total += inputs[i]

print(max_cals)
