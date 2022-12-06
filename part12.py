with open('input6.txt', 'r') as f:
    inputs = f.readlines()[0].strip('\n')

for i in range(1, len(inputs)-14):
    ins = inputs[i-1:i+13]
    x = 0
    for j in range(len(ins)):
        for k in range(len(ins)):
            if not j == k:
                if ins[j] == ins[k]:
                    x = 1
    if x == 0:
        print(ins, i+13)
        break
    pass
