class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

        print(f"Enter elements for {rows} x {cols} matrix:")
        for i in range(rows):
            row = list(map(int, input().split()))
            self.matrix.append(row)
    def __add__(self, other):
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)

        return result

    def __sub__(self, other):
        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)

        return result

    def __mul__(self, other):
        result = []

        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                total = 0
                for k in range(self.cols):
                    total += self.matrix[i][k] * other.matrix[k][j]
                row.append(total)
            result.append(row)

        return result
    @staticmethod
    def display(matrix):
        for row in matrix:
            print(row)
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix A")
A = Matrix(rows, cols)

print("Enter Matrix B")
B = Matrix(rows, cols)
print("Matrix Addition:")
Matrix.display(A + B)
print("Matrix Subtraction:")
Matrix.display(A - B)

print("Matrix Multiplication:")
Matrix.display(A * B)
