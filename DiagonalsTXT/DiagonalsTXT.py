a = [[int(i) for i in x.strip().split()] for x in open("matrix.txt", "r").readlines()]
b = [0] * len(a)
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="  ")
        b[j - i] += a[i][j]
    print()
print("\nDiagonals: " + str(b) + "\n\nMax: " + str(max(b)))