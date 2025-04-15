# Deklarasi Matriks
matriksA = [
    [1,2,3,4,5],
    [3,2,5,4,6],
    [7,9,1,0,1],
    [0,2,4,6,8],
    [1,3,5,7,9]
]
matriksB = [
    [6,7,8,9,10],
    [1,6,2,1,3],
    [0,0,4,1,9],
    [2,10,5,8,0],
    [6,9,0,3,10]
]
matriksC = []

# Perkalian matriks
for i in range(0, len(matriksA), 1):
    matriksC.append([])
    for j in range(0, len(matriksB[0]), 1):
        temp_res = 0
        for k in range(0, len(matriksB), 1):
            temp_res += matriksA[i][k]*matriksB[k][j]
        matriksC[i].append(temp_res)

# Tampilkan hasil matriks
for row in matriksC:
    print(row)
