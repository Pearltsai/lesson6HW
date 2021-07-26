names=['Chris','David','Bill','Amy','james']
scores=[83,96,92,59,77]
M=scores[0]
i=0
while i<5:
    if M<=scores[i]:
        M=scores[i]
    i=i+1
print('最高分是',M)
place=scores.index(M)
print('最高分是',names[place])