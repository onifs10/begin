dim = int(input('dimention ?'))
def diagonalDiff(Mat):
    x = 0
    y = 0
    for i in range(dim):
        y += Mat[i][dim-(1+i)]
        x += Mat[i][i]
    return abs(x - y) 
Mat = []
for j in range(dim):
    Mat.append(list(map(int,input().rstrip().split())))
print(diagonalDiff(Mat))
