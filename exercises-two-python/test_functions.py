import unittest
from can_construct import can_construct
from contains_duplicate import contains_duplicate
from first_occurrence import first_occurrence
from happy_number import is_happy


class TestWorkspaceFunctions(unittest.TestCase):
    # Tests for can_construct
    def test_can_construct_basic(self):
        self.assertTrue(can_construct("a", "ab"))

    def test_can_construct_impossible(self):
        self.assertFalse(can_construct("a", "b"))

    def test_can_construct_multi_chars(self):
        self.assertTrue(can_construct("aa", "aab"))

    def test_can_construct_empty_note(self):
        self.assertTrue(can_construct("", "abc"))

    def test_can_construct_insufficient(self):
        self.assertFalse(can_construct("aaa", "aa"))

    # Tests for contains_duplicate
    def test_contains_duplicate_true(self):
        self.assertTrue(contains_duplicate([1, 2, 3, 1], 3))

    def test_contains_duplicate_false(self):
        self.assertFalse(contains_duplicate([1, 2, 3, 4], 2))

    def test_contains_duplicate_adjacent(self):
        self.assertTrue(contains_duplicate([1, 0, 1, 1], 1))

    def test_contains_duplicate_empty(self):
        self.assertFalse(contains_duplicate([], 5))

    # Tests for first_occurrence
    def test_first_occurrence_basic(self):
        self.assertEqual(first_occurrence("hello", "ll"), 2)

    def test_first_occurrence_not_found(self):
        self.assertEqual(first_occurrence("hello", "z"), -1)

    def test_first_occurrence_empty_haystack(self):
        self.assertEqual(first_occurrence("", "a"), -1)

    def test_first_occurrence_complex(self):
        self.assertEqual(first_occurrence("mississippi", "issi"), 1)

    # Tests for happy_number functions
    def test_is_happy_true(self):
        self.assertTrue(is_happy(19))

    def test_is_happy_false(self):
        self.assertFalse(is_happy(2))

    def test_is_happy_one(self):
        self.assertTrue(is_happy(1))


if __name__ == "__main__":
    unittest.main()
