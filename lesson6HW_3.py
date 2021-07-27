
scores=[['Chris',83],['David',96],['Bill',92],['Amy',59],['james',77]]
M=scores[0][1]
i=0
while i<5:
    if M<scores[i][1]:
        M=scores[i][1]
        j=i
    i=i+1
print(M)
print(scores[j][0])