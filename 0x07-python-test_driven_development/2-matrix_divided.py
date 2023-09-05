def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the divided elements.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        ValueError: If the rows of the matrix have different sizes.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is zero.

    """

    # Validate the matrix parameter
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a matrix (list of lists) of integers/floats.")

    # Get the size of the first row for comparison
    row_size = len(matrix[0])

    # Check if all rows have the same size
    if not all(len(row) == row_size for row in matrix):
        raise ValueError("All rows of the matrix must have the same size.")

    # Validate the div parameter
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number.")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero.")

    # Perform the division and create a new matrix
    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix
