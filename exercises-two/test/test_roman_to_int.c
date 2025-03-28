#include "../include/roman_to_int.h"
#include "../test/unity/unity.h"

void setUp(void) {}

void tearDown(void) {}

void test_roman_to_integer_less_than_ten(void) {
  TEST_ASSERT_EQUAL_INT(3, roman_to_int("III"));
}

void test_roman_to_integer_basic(void) {
  TEST_ASSERT_EQUAL_INT(58, roman_to_int("LVIII"));
}

void test_roman_to_integer_all_cases(void) {
  TEST_ASSERT_EQUAL_INT(3749, roman_to_int("MMMDCCXLIX"));
}

int main(void) {
  UNITY_BEGIN();
  RUN_TEST(test_roman_to_integer_less_than_ten);
  RUN_TEST(test_roman_to_integer_basic);
  RUN_TEST(test_roman_to_integer_all_cases);
  return UNITY_END();
}
