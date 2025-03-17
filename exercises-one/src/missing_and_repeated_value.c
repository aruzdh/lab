#include "../include/missing_and_repeated_value.h"
#include <stdlib.h>

int *missing_and_repeated_value(int **matrix, int size) {
  int total_numbers = size * size;
  int total_sum = 0;
  int repeated_num = 0;

  int *seen = calloc(total_numbers + 1, sizeof(int));
  if (seen == NULL) {
    return NULL;
  }

  int *ans = malloc(2 * sizeof(int));
  if (ans == NULL) {
    free(seen);
    return NULL;
  }

  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      int elem = matrix[i][j];
      if (seen[elem]) {
        repeated_num = elem;
      } else {
        seen[elem] = 1;
        total_sum += elem;
      }
    }
  }

  int expected_sum = (total_numbers * (total_numbers + 1)) / 2;
  int missing_number = expected_sum - total_sum;

  ans[0] = repeated_num;
  ans[1] = missing_number;

  free(seen);
  return ans;
}
