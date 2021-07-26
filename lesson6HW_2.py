scores=['Chris',83,'David',96,'Bill',92,'Amy',59,'james',77]
M=scores[1]
for i in range(1,10,2):
    if M<=scores[i]:
        M=scores[i]
y=scores.index(M)
x=scores[y-1]
print('最高分是',M,x)

