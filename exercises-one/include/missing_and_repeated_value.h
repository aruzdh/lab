#ifndef MISSING_AND_REPEATED_VALUE_H
#define MISSING_AND_REPEATED_VALUE_H

/*
 * Identifies the missing and repeated values in a square matrix.
 * The matrix is assumed to contain numbers from 1 to size*size, with one number
 * missing and one repeated.
 * @param matrix A pointer to a 2D array (square matrix) of integers.
 * @param size The number of rows (and columns) in the matrix (must be
 * greater than or equal to two).
 * @return A pointer to a dynamically allocated array of 2 integers:
 *         - result[0]: the repeated value.
 *         - result[1]: the missing value.
 *         Returns NULL if memory allocation fails.
 * @note The caller is responsible for freeing the returned array.
 *
 * The algorithm has a time complexity of O(n^2), where n is the size of the
 * matrix, and a space complexity of O(n^2), as it uses an array to track seen
 * elements in the matrix,
 */
int *missing_and_repeated_value(int **matrix, int size);

#endif
