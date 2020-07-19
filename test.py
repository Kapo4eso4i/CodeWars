newp = 8000
doublem = 0
persent = 1.5
for i in range(6):
    newp = ((newp / 100) * (100 - persent))
    doublem += 1
    if doublem == 2:
        persent += 0.5
        doublem = 0
    print(i, newp)
