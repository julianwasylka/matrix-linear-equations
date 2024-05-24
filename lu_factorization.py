import time

def lu_factorization(A, b, save=False):
    start_time = time.time()

    L, U = A.lu_decomposition()
    y = L.forward_substitution(b)
    x = U.backward_substitution(y)

    end_time = time.time()
    exe_time = end_time - start_time

    if save:
        with open('times.txt', 'a') as file:
            file.write(f'LU for N={A.n}: time - {exe_time}\n')

    return x, exe_time
