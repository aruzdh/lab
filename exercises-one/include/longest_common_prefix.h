#ifndef LONGEST_COMMON_PREFIX_H
#define LONGEST_COMMON_PREFIX_H

/*
 * Finds the longest common prefix among an array of strings.
 * @param strs An array of pointers to null-terminated strings.
 * @param strs_size The number of strings in the array (must be between 1 and
 * 200).
 * @return A pointer to a dynamically allocated string containing the longest
 * common prefix. Returns NULL if memory allocation fails.
 * @note The caller is responsible for freeing the returned string.
 */
char *longest_common_prefix(char **strs, int strs_size);

#endif
