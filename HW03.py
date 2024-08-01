def isSparse(n, m, A):
    count = 0
    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                count += 1
    if count > (n * m) / 2:
        return 0
    else:
        return 1

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))

A = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input("Enter element at position ({}, {}): ".format(i+1, j+1)))
        row.append(element)
    A.append(row)


print("Matrix:")
for i in range(n):
    for j in range(m):
        print("{:^4}".format(A[i][j]), end=' ')
    print()


result = isSparse(n, m, A)
if result == 1:
    print("The matrix is sparse.")
    print("Non-zero elements:")
    for i in range(n):
        for j in range(m):
            if A[i][j] != 0:
                print("({}, {}, {})".format(i+1, j+1, A[i][j]))
else:
    print("The matrix is not sparse.")
