with open('input4.txt', 'r') as f:
    inputs = f.readlines()

for i in range(len(inputs)):
    inputs[i] = inputs[i].strip('\n')

contain_pairs = 0

for ins in inputs:
    ins = ins.split(',')
    elf1 = [int(a) for a in ins[0].split('-') ]
    elf2 = [int(a) for a in ins[1].split('-') ]
    
    lelf1 = [(a) for a in range(elf1[0], elf1[1]+1)]
    lelf2 = [(a) for a in range(elf2[0], elf2[1]+1)]

    if len(lelf1) > len(lelf2):
        if any(item in lelf1 for item in lelf2):
            contain_pairs += 1
    else:
        if any(item in lelf2 for item in lelf1):
            contain_pairs += 1

print(contain_pairs)
