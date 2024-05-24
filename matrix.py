import math

class Matrix:
    def __init__(self, n, m, filling=0, matrix=None):
        self.n = n
        self.m = m
        self.matrix = [[filling for _ in range(m)] for _ in range(n)]
        if matrix != None: self.matrix = matrix

    def copy(self):
        copied_matrix = [row[:] for row in self.matrix]
        new_matrix = Matrix(self.n, self.m, matrix=copied_matrix)
        return new_matrix
    
    def times_minus_one(self, type=None):
        result = self.copy()
        if type == "D":
            for i in range(result.n):
                result.matrix[i][i] *= -1
        else:
            for i in range(result.n):
                for j in range(i+1):
                    result.matrix[i][j] *= -1   
        return result

    def __mul__(self, other):
        if self.m != other.n:
            raise ValueError("multiply - Matrix dimensions don't match")

        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                result.matrix[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(self.m))
        
        return result
    
    def __add__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("add - Matrix dimensions don't match")
        
        result = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return result

    def __sub__(self, other):
        if self.n != other.n or self.m != other.m:
            raise ValueError("add - Matrix dimensions don't match")
        
        result = Matrix(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.matrix[i][j] = self.matrix[i][j] - other.matrix[i][j]
        return result

    def forward_substitution(self, B):
        if self.n != B.n:
            raise ValueError("Dimension mismatch between matrix and vector")
        
        x = Matrix(self.n, B.m)
        
        for k in range(B.m): #B columns (if vector - 1 iteration)
            for i in range(self.n):
                if self.matrix[i][i] == 0:
                    raise ValueError("Matrix is singular")
                
                x.matrix[i][k] = B.matrix[i][k]
                for j in range(i):
                    x.matrix[i][k] -= self.matrix[i][j] * x.matrix[j][k]
                x.matrix[i][k] /= self.matrix[i][i]
        
        return x
    
    def backward_substitution(self, B):
        if self.n != B.n:
            raise ValueError("Dimension mismatch between matrix and vector")
        
        x = Matrix(self.n, B.m)
        
        for k in range(B.m):  # B columns (if vector - 1 iteration)
            for i in range(self.n - 1, -1, -1):
                if self.matrix[i][i] == 0:
                    raise ValueError("Matrix is singular")
                
                x.matrix[i][k] = B.matrix[i][k]
                for j in range(i + 1, self.n):
                    x.matrix[i][k] -= self.matrix[i][j] * x.matrix[j][k]
                x.matrix[i][k] /= self.matrix[i][i]
        
        return x

    def norm(self):
        norm = 0
        try:
            for row in self.matrix:
                for val in row:
                    norm += val ** 2
            return math.sqrt(norm)
        except OverflowError:
            return float('inf')
