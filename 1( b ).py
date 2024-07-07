def main():
    # Define the matrix A from part (b)
    A2 = np.array([
        [12, 10, -6, -3, 7, 10],
        [-7, -6, 4, 7, -9, 5],
        [9, 9, -9, -5, 5, -1],
        [-4, -3, 1, 6, -8, 9],
        [8, 7, -5, -9, 11, -8]
    ])

    # Perform row reduction and identify pivot columns
    U2 = row_echelon_form(A2)
    pivot_columns2 = find_pivot_columns(U2)
    B2 = construct_B(A2, pivot_columns2)

    # Display results
    print("Matrix A (part b):")
    print(A2)
    print("\nRow echelon form of A:")
    print(U2)
    print("\nPivot columns of A:", pivot_columns2)
    print("\nMatrix B (part b):")
    print(B2)

    # Verify Bx = 0 has only the trivial solution
    if verify_trivial_solution(B2):
        print("\nVerification: B2 * x = 0 has only the trivial solution.")
    else:
        print("\nVerification: B2 * x = 0 has non-trivial solutions.")

if __name__ == "__main__":
    main()

