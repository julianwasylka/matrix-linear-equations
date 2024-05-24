import time
from matrix import Matrix

def jacobi(N, A, b, iterations, tolerance, save=False):
    L, D, U = A.partition()
    x = Matrix(N, 1, 1)
    minus_D = D.times_minus_one(type="D")

    M = minus_D.forward_substitution(L + U)
    bm = D.forward_substitution(b)
    start_time = time.time()

    norms = []
    err_norm = (A * x - b).norm()
    norms.append(err_norm)
    i = 0

    while err_norm > tolerance and i < iterations:
        x_prev = x.copy()
        x = M * x_prev + bm
        err_norm = (A * x - b).norm()
        norms.append(err_norm)
        i += 1
        print(err_norm)

    end_time = time.time()
    exe_time = end_time - start_time

    if save:
        with open('times.txt', 'a') as file:
            file.write(f'Jacobi for N={N}: time - {exe_time}, iterations - {i}\n')

    return x, i, norms, exe_time