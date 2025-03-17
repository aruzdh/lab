#include "../include/missing_and_repeated_value.h"
#include "../test/unity/unity.h"
#include <stdlib.h>

void setUp(void) {}
void tearDown(void) {}

void test_missing_and_repeated_value_2x2(void) {
  int matrix[2][2] = {{1, 3}, {2, 2}};
  int *matrix_ptr[2] = {matrix[0], matrix[1]};
  int *result = missing_and_repeated_value(matrix_ptr, 2);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_INT(2, result[0]);
  TEST_ASSERT_EQUAL_INT(4, result[1]);
  free(result);
}

void test_missing_and_repeated_value_3x3(void) {
  int matrix[3][3] = {{1, 2, 3}, {4, 5, 6}, {5, 8, 9}};
  int *matrix_ptr[3] = {matrix[0], matrix[1], matrix[2]};
  int *result = missing_and_repeated_value(matrix_ptr, 3);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_INT(5, result[0]);
  TEST_ASSERT_EQUAL_INT(7, result[1]);
  free(result);
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_missing_and_repeated_value_2x2);
  RUN_TEST(test_missing_and_repeated_value_3x3);
  return UNITY_END();
}
