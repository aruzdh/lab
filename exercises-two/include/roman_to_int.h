#ifndef ROMAN_TO_INT_H
#define ROMAN_TO_INT_H

/*
 * Converts a Roman numeral string to its integer value.
 * @param roman A pointer to a null-terminated string representing a valid Roman
 * numeral.
 * @return The integer equivalent of the Roman numeral characters.
 *
 * The algorithm has a time complexity of O(n), where n is the length of the
 * input string, and a space complexity of O(1) since it does not use any
 * additional space.
 */
int roman_to_int(char *roman);

#endif
