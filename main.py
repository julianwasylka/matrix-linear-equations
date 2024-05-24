import matplotlib.pyplot as plt
from matrix_types import A_band, B_sin
from jacobi import jacobi
from gauss_seidel import gauss_seidel
from lu_factorization import lu_factorization

N = 923 #index = 193223

def part_1(save_plot=False):
    e = 2
    a1 = 5 + e
    a2 = a3 = -1
    A = A_band(N, a1, a2, a3)
    b = B_sin(N)

    x_j, iterations_j, norms_j, time_j = jacobi(N, A, b, 1000, 10**(-9), save=True)
    print(f"Jacobi: iterations - {iterations_j}, time - {time_j}")
    
    x_gs, iterations_gs, norms_gs, time_gs = gauss_seidel(N, A, b, 1000, 10**(-9), save=True)
    print(f"Gauss-Seidel: iterations - {iterations_gs}, time - {time_gs}")

    plt.plot(norms_j, label='Jacobi norm')
    plt.plot(norms_gs, label='Gauss-Seidel norm')

    plt.yscale('log')
    plt.title('Change of Residual Norms')
    plt.xlabel('Iterations')
    plt.ylabel('Residual Norm Value')

    plt.legend()
    if save_plot: plt.savefig('task_B.png')
    plt.show()

def part_2(save_plot=False):
    a1 = 3
    a2 = a3 = -1
    A = A_band(N, a1, a2, a3)
    b = B_sin(N)

    x_j, iterations_j, norms_j, time_j = jacobi(N, A, b, 1000, 10**(-9))
    print(f'Jacobi: iterations - {iterations_j}, time - {time_j}')

    x_gs, iterations_gs, norms_gs, time_gs = gauss_seidel(N, A, b, 1000, 10**(-9))
    print(f'Gauss-Seidel: iterations - {iterations_gs}, time - {time_gs}')

    plt.plot(norms_j, label='Jacobi norm')
    plt.plot(norms_gs, label='Gauss-Seidel norm')

    plt.yscale('log')
    plt.title('Change of Residual Norms')
    plt.xlabel('Iterations')
    plt.ylabel('Residual Norm Value')

    plt.legend()
    if save_plot: plt.savefig('task_C.png')
    plt.show()

def part_3():
    a1 = 3
    a2 = a3 = -1
    A = A_band(N, a1, a2, a3)
    b = B_sin(N)

    x, time_lu = lu_factorization(A, b, save=False)
    print(f'LU factorization: time - {time_lu}, Residual Norm - {(A * x - b).norm()}')

def part_4(save_plot=False):
    n_tab = [100, 500, 1000, 2000, 3000]
    j_times = []
    gs_times = []
    lu_times = []

    e = 2
    a1 = 5 + e
    a2 = a3 = -1

    for n in n_tab:
        A = A_band(n, a1, a2, a3)
        b = B_sin(n)
        _, _, _, time_j = jacobi(n, A, b, 1000, 10**(-9), save=True)
        j_times.append(time_j)
        _, _, _, time_gs = gauss_seidel(n, A, b, 1000, 10**(-9), save=True)
        gs_times.append(time_gs)
        _, time_lu = lu_factorization(A, b, save=True)
        lu_times.append(time_lu)

    plt.plot(n_tab, j_times, label='Jacobi times')
    plt.plot(n_tab, gs_times, label='Gauss-Seidel times')
    plt.plot(n_tab, lu_times, label='LU factorization times')

    plt.title('Execution Times for Different Methods')
    plt.xlabel('Matrix Size (n)')
    plt.ylabel('Time (seconds)')

    plt.legend()
    if save_plot: plt.savefig('task_E.png')
    plt.show()


if __name__ == "__main__":
    #part_1(save_plot=False)
    #part_2(save_plot=False)
    part_3()
    #part_4(save_plot=True)