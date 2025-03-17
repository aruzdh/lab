#include "../include/longest_common_prefix.h"
#include <stdlib.h>
#include <string.h>

char *longest_common_prefix(char **strs, int strs_size) {
  if (strs_size == 1) {
    size_t len = strlen(strs[0]) + 1;
    char *copy = malloc(len * sizeof(char));
    if (copy == NULL)
      return NULL;
    strcpy(copy, strs[0]);
    return copy;
  }
  if (strs[0][0] == '\0') {
    char *empty = malloc(1 * sizeof(char));
    if (empty == NULL)
      return NULL;
    empty[0] = '\0';
    return empty;
  }

  char *pivot = strs[0];
  size_t pivot_len = strlen(pivot);
  int prefix_len = 0;

  for (size_t i = 0; i < pivot_len; i++) {
    char curr_letter = pivot[i];

    for (int j = 1; j < strs_size; j++) {
      if (i >= strlen(strs[j]) || strs[j][i] != curr_letter) {
        char *lcp = malloc((prefix_len + 1) * sizeof(char));
        if (lcp == NULL)
          return NULL;
        strncpy(lcp, pivot, prefix_len);
        lcp[prefix_len] = '\0';
        return lcp;
      }
    }
    prefix_len++;
  }

  char *lcp = malloc((pivot_len + 1) * sizeof(char));
  if (lcp == NULL)
    return NULL;
  strcpy(lcp, pivot);
  return lcp;
}
