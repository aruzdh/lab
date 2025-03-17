#ifndef INT_TO_ROMAN_H
#define INT_TO_ROMAN_H

/*
 * Converts an integer to its Roman numeral representation.
 * @param num The integer to convert (must be between 1 and 3999).
 * @return A pointer to a dynamically allocated string containing the Roman
 * numeral. Returns NULL if memory allocation fails.
 * @note The caller is responsible for freeing the returned string.
 */
char *int_to_roman(int num);

#endif
