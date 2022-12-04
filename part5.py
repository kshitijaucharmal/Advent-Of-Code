sample = []
with open('input3.txt', 'r') as f:
    sample = f.readlines()

for i in range(len(sample)):
    sample[i] = sample[i].strip('\n')

letters = {}
for i in range(97, 97+26):
    letters[chr(i)] = i - 96
for i in range(65, 65 + 26):
    letters[chr(i)] = i - 65 + 27

total_priority = 0
for s in sample:
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2:]
    for l in s1:
        x = 0
        if l in s2:
            x = 1
            # print(l, letters[l])
            total_priority += letters[l]
        if x == 1:
            break
print(total_priority)
