#include "../include/int_to_roman.h"
#include <stdlib.h>
#include <string.h>

char *int_to_roman(int num) {
  int values[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
  char *symbols[] = {"M",  "CM", "D",  "CD", "C",  "XC", "L",
                     "XL", "X",  "IX", "V",  "IV", "I"};

  char *result = malloc(16 * sizeof(char));
  if (result == NULL) {
    return NULL;
  }

  result[0] = '\0';

  int i = 0;
  while (num > 0) {
    while (num >= values[i]) {
      strcat(result, symbols[i]);
      num -= values[i];
    }
    i++;
  }

  return result;
}
