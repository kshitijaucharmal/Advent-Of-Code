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

win = {
    1:2,
    2:3,
    3:1
}
lose = {
    1:3,
    2:1,
    3:2
}

# m is Lose, draw, or win
def win_draw_lose(e, m):
    score = 0
    # Draw
    if m == 2:
        move = e
        score = move + 3
    # Lose
    if m == 1:
        move = lose[e]
        score = move + 0
    # Win
    if m == 3:
        move = win[e]
        score = move + 6
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
