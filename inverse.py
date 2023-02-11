import copy

def inputMatrix():
    rows = int(input("Enter number of rows of matrix:"))
    cols = int(input("Enter number of columns of matrix:"))
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            number = float(input(f"Enter the number for row {i+1} and column {j+1}:"))
            row.append(number)
        matrix.append(row)
    return matrix

def findDeterminant(matrix):
    """In this method,we first reduce the matrix to row echelon form and then,multilpy the
    diagonal elements"""
    ans = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if row == col:
                pe = matrix[row][col]
                ans.append(pe)  # Stores the diagonal elements
                if pe != 0:
                    for r in range(len(matrix[0])):
                        matrix[row][r] = round(matrix[row][r] / pe, 3)
                    for j in range(len(matrix)):
                        if j > row:
                            makeZero = matrix[j][col]
                            for k in range(len(matrix[0])):
                                matrix[j][k] = round(matrix[j][k] - matrix[row][k] * makeZero, 3)
    result = 1
    for r in range(len(ans)):
        result *= ans[r] # Multiplying all the diagonal elements to get the determinant
    return round(result)

def findMinor(mat,x,y):
    """In this part,we are calculating the determinant"""
    res = findDeterminant(mat)
    # This part checks for the sign of the cofactor
    signOfCofactor = x + y
    if signOfCofactor % 2 == 0: # If the position of number is even,then,don't change the sign
        return res
    else:  # Otherwise,change the sign of the cofactor
        res *= -1
        return res

def printMatrix(adjMatrix):
    for i in adjMatrix:
        for j in i:
            print("%10.3F" % j, end=" ")
        print()

def findTranspose(coMatrix,oMatrix):
    adjointMatrix = []
    for i in range(len(coMatrix)):
        rows = []
        for j in range(len(oMatrix[0])):
            num = coMatrix[j][i]
            rows.append(num)
        adjointMatrix.append(rows)
    return adjointMatrix

def findAdjoint(m):
    cofactorMatrix = [] # It stores the minors of every position i,j
    for i in range(len(m)):
        r = []
        for j in range(len(m[0])):
            newMinorMatrix = [] # It returns a new minor matrix for each number
            for k in range(len(m)):
                row = []
                for l in range(len(m[0])):
                    if k == i: # It is for the deletion of row
                        continue
                    elif l == j: # It is for the deletion of column
                        continue
                    else:
                        row.append(m[k][l])
                if row != []:
                    newMinorMatrix.append(row)
            # It returns the cofactor of every position i,j
            Cofactor = findMinor(newMinorMatrix, i, j)
            r.append(Cofactor)
        cofactorMatrix.append(r)
    # It will return the transpose of cofactor matrix
    adjointMatrix = findTranspose(cofactorMatrix, m)
    return adjointMatrix

def findInverse():
    matrix = inputMatrix()
    # Making a deepcopy because the matrix will get change after determinant operation and in most of the
    # places we will need original matrix
    copyMatrix = copy.deepcopy(matrix)
    determinant = findDeterminant(matrix)
    if determinant != 0:
        print("It's a non-singular matrix.The inverse is:")
        adjMatrix = findAdjoint(copyMatrix)
        # inverse = adjoint / determinant
        # This code divides the each element of adjoint matrix by determinantcopy.deep
        inverseMatrix = []
        for i in range(len(adjMatrix)):
            row = []
            for j in range(len(adjMatrix[0])):
                entry = adjMatrix[i][j] / determinant
                row.append(entry)
            inverseMatrix.append(row)
        # This will print the result
        printMatrix(inverseMatrix)
    else:
        print("It's a singular matrix.So the inverse can't be calculated.")

findInverse()
