#include "../include/longest_common_prefix.h"
#include "../test/unity/unity.h"
#include <stdlib.h>

void setUp(void) {}
void tearDown(void) {}

void test_longest_common_prefix_basic(void) {
  char *strs[] = {"flower", "flow", "flight"};
  char *result = longest_common_prefix(strs, 3);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_STRING("fl", result);
  free(result);
}

void test_longest_common_prefix_no_common(void) {
  char *strs[] = {"dog", "cat", "rat"};
  char *result = longest_common_prefix(strs, 3);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_STRING("", result);
  free(result);
}

void test_longest_common_prefix_single_string(void) {
  char *strs[] = {"flower"};
  char *result = longest_common_prefix(strs, 1);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_STRING("flower", result);
  free(result);
}

void test_longest_common_prefix_empty_first(void) {
  char *strs[] = {"", "flow", "flight"};
  char *result = longest_common_prefix(strs, 3);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_STRING("", result);
  free(result);
}

void test_longest_common_prefix_just_empty_str(void) {
  char *strs[] = {""};
  char *result = longest_common_prefix(strs, 1);

  TEST_ASSERT_NOT_NULL(result);
  TEST_ASSERT_EQUAL_STRING("", result);
  free(result);
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_longest_common_prefix_basic);
  RUN_TEST(test_longest_common_prefix_no_common);
  RUN_TEST(test_longest_common_prefix_single_string);
  RUN_TEST(test_longest_common_prefix_just_empty_str);
  RUN_TEST(test_longest_common_prefix_empty_first);
  return UNITY_END();
}
