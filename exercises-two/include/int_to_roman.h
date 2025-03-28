#ifndef INT_TO_ROMAN_H
#define INT_TO_ROMAN_H

/*
 * Converts an integer to its Roman numeral representation.
 * @param num The integer to convert (must be between 1 and 3999).
 * @return A pointer to a dynamically allocated string containing the Roman
 * numeral. Returns NULL if memory allocation fails.
 * @note The caller is responsible for freeing the returned string.
 *
 * The algorithm has a time complexity of O(n), where n is the value of the
 * input number, and a space complexity of O(1), as the size of the result
 * string is fixed and does not depend on the input.
 */
char *int_to_roman(int num);

#endif
