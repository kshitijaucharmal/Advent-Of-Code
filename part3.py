# A - Rock
# B - Paper
# C - Scissor
# X - Rock
# Y - Paper
# Z - Scissor

# 1, 2, 3 + 
# 0 lost, 3 draw, 6 win
# = total score

def con(val):
    if val in ['A', 'X']:
        return 1
    if val in ['B', 'Y']:
        return 2
    if val in ['C', 'Z']:
        return 3

def win_draw_lose(e, m):
    score = 0
    if e == m:
        score = m + 3
    if e == 1:
        if m == 2:
            score = m + 6
        if m == 3:
            score = m
    if e == 2:
        if m == 3:
            score = m + 6
        if m == 1:
            score = m
    if e == 3:
        if m == 1:
            score = m + 6
        if m == 2:
            score = m
    return score

inputs = []
with open('input2.txt', 'r') as f:
    inputs = f.readlines()
for i in range(len(inputs)):
    inputs[i] = inputs[i].strip('\n')

res = 0
for i in range(len(inputs)):
    ins = inputs[i]
    elf_move = con(ins[0])
    my_move = con(ins[2])
    res += win_draw_lose(elf_move, my_move)
print(res)
