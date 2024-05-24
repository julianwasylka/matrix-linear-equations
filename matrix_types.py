import math
from matrix import Matrix

class A_band(Matrix):
    def __init__(self, N, a1, a2, a3):
        super().__init__(N, N) 
        self.N = N
        self.matrix[0][0] = a1
        self.matrix[0][1] = a2
        self.matrix[1][0] = a2
        self.matrix[1][1] = a1
        for i in range(2, N):
            self.matrix[i][i] = a1
            self.matrix[i-1][i] = a2
            self.matrix[i][i-1] = a2
            if i - 2 >= 0:
                self.matrix[i-2][i] = a3
                self.matrix[i][i-2] = a3

    def partition(self):
        L = Matrix(self.N, self.N)
        D = Matrix(self.N, self.N)
        U = Matrix(self.N, self.N)

        for i in range(self.N):
            for j in range(self.N):
                if i == j:
                    D.matrix[i][j] = self.matrix[i][j]
                elif i > j:
                    L.matrix[i][j] = self.matrix[i][j]
                else:
                    U.matrix[i][j] = self.matrix[i][j]
        
        return L, D, U
    
    def lu_decomposition(self):
        U = self.copy()
        L = eye(self.N)

        for i in range(2, self.N + 1):
            for j in range(1, i):
                a = L.matrix[i - 1][j - 1] = U.matrix[i - 1][j - 1] / U.matrix[j - 1][j - 1]
                for k in range(self.N):
                    U.matrix[i-1][k] -= a * U.matrix[j-1][k]
                #U.matrix[i - 1][:] = U.matrix[i - 1][:] - L.matrix[i - 1][j - 1] * U.matrix[j - 1][:]

        return L, U


class B_sin(Matrix):
    def __init__(self, N):
        super().__init__(N, 1)
        f = 3 + 1 #index = 193223
        self.matrix = [[math.sin(i * f) for _ in range(self.m)] for i in range(self.n)]

def eye(n):
    result = Matrix(n, n)
    for i in range(n):
        result.matrix[i][i] = 1

    return result
