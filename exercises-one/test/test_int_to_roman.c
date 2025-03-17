
#include "../include/int_to_roman.h"
#include "../test/unity/unity.h"
void setUp(void) {}

void tearDown(void) {}

void test_int_to_roman_less_than_ten(void) {
  TEST_ASSERT_EQUAL_STRING("III", int_to_roman(3));
}

void test_int_to_roman_basic(void) {
  TEST_ASSERT_EQUAL_STRING("LVIII", int_to_roman(58));
}

void test_int_to_roman_all_cases(void) {
  TEST_ASSERT_EQUAL_STRING("MMMDCCXLIX", int_to_roman(3749));
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_int_to_roman_less_than_ten);
  RUN_TEST(test_int_to_roman_basic);
  RUN_TEST(test_int_to_roman_all_cases);
  return UNITY_END();
}
