import numpy as np
from scipy.linalg import lu

def row_echelon_form(A):
    P, L, U = lu(A)
    return U

def find_pivot_columns(U):
    pivots = []
    for i in range(U.shape[0]):
        for j in range(U.shape[1]):
            if U[i, j] != 0:
                pivots.append(j)
                break
    return pivots

def construct_B(A, pivot_columns):
    return A[:, pivot_columns]

def verify_trivial_solution(B):
    return np.linalg.matrix_rank(B) == B.shape[1]

def main():
    # Define the matrix A from part (a)
    A1 = np.array([
        [8, -3, 0, -7, 2],
        [-9, 4, 5, 11, -7],
        [6, -2, 2, -4, 4],
        [5, -1, 7, 0, 10]
    ])

    # Perform row reduction and identify pivot columns
    U1 = row_echelon_form(A1)
    pivot_columns1 = find_pivot_columns(U1)
    B1 = construct_B(A1, pivot_columns1)

    # Display results
    print("Matrix A (part a):")
    print(A1)
    print("\nRow echelon form of A:")
    print(U1)
    print("\nPivot columns of A:", pivot_columns1)
    print("\nMatrix B (part a):")
    print(B1)

    # Verify Bx = 0 has only the trivial solution
    if verify_trivial_solution(B1):
        print("\nVerification: B1 * x = 0 has only the trivial solution.")
    else:
        print("\nVerification: B1 * x = 0 has non-trivial solutions.")

if __name__ == "__main__":
    main()
