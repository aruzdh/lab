#include "../include/roman_to_int.h"

int get_value(char roman) {
  switch (roman) {
  case 'I':
    return 1;
  case 'V':
    return 5;
  case 'X':
    return 10;
  case 'L':
    return 50;
  case 'C':
    return 100;
  case 'D':
    return 500;
  case 'M':
    return 1000;
  default:
    return 0;
  }
}

int roman_to_int(char *roman) {
  int total = 0;
  for (int i = 0; roman[i] != '\0'; ++i) {
    if (get_value(roman[i]) < get_value(roman[i + 1])) {
      total -= get_value(roman[i]);
    } else {
      total += get_value(roman[i]);
    }
  }
  return total;
}
