# Time complexity is O(m * n) where m is the number of rows and n is the number of columns, with O(1) extra space.
def set_zeroes(matrix):
    """
    Sets entire rows and columns to zero in place if a cell in the matrix is zero.

    Args:
        matrix (List[List[int]]): A 2D list of integers representing the matrix.

    Returns:
        None: The matrix is modified in place.
    """
    first_row = False
    first_col = False
    num_rows = range(len(matrix))
    num_cols = range(len(matrix[0]))

    for row in num_rows:
        for col in num_cols:
            if matrix[row][col] == 0:
                if row == 0:
                    first_row = True
                if col == 0:
                    first_col = True

                matrix[0][col] = None
                matrix[row][0] = None

    for col in range(1, len(matrix[0])):
        if matrix[0][col] is None:
            for row in num_rows:
                matrix[row][col] = 0

    for row in range(1, len(matrix)):
        if matrix[row][0] is None:
            for col in num_cols:
                matrix[row][col] = 0

    if first_col:
        for row in num_rows:
            matrix[row][0] = 0

    if first_row:
        for col in num_cols:
            matrix[0][col] = 0
