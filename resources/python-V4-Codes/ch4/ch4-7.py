##### driver program   ------------------    
from matModule import *
r = 3
c = 5
mat = np.matrix([([0] * c) for i in range(r)])
generate(mat)
print("Original matrix :")
printMat(mat)
print("---------------------------------")
print("The elements on first diagonal : ")
firstDiagonal(mat)
print("---------------------------------")
print("The elements on second diagonal :")
secDiagonal(mat)
print("---------------------------------")
print("Sum of rows: ")
print("---------------------------------")
sumofRows(mat)
print("---------------------------------")
print("Sum of columns :")
print("---------------------------------")
sumofCols(mat)

