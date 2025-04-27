import unittest
from set_zeroes import set_zeroes
from single_number import single_number
from merge_intervals import merge_intervals
from has_cycle import ListNode, has_cycle


class TestWorkspaceFunctions(unittest.TestCase):
    # Tests for set_zeroes
    def test_set_zeroes_basic(self):
        matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        expected = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
        set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_multiple_zeros(self):
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        expected = [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
        set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_multiple_cases(self):
        matrix = [
            [8, 3, 6, 9, 7, 8, 0, 6],
            [0, 3, 7, 0, 0, 4, 3, 8],
            [5, 3, 6, 7, 1, 6, 2, 6],
            [8, 7, 2, 5, 0, 6, 4, 0],
            [0, 2, 9, 9, 3, 9, 7, 3],
        ]
        expected = [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 3, 6, 0, 0, 6, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
        set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_single_row(self):
        matrix = [[1, 0, 3]]
        expected = [[0, 0, 0]]
        set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    def test_set_zeroes_single_col(self):
        matrix = [[1], [0], [3]]
        expected = [[0], [0], [0]]
        set_zeroes(matrix)
        self.assertEqual(matrix, expected)

    # Tests for single_number
    def test_single_number_simple(self):
        self.assertEqual(single_number([2, 2, 1]), 1)

    def test_single_number_unsorted(self):
        self.assertEqual(single_number([4, 1, 2, 1, 2]), 4)

    def test_single_number_single_element(self):
        self.assertEqual(single_number([7]), 7)

    def test_single_number_negative(self):
        self.assertEqual(single_number([-1, -1, -2]), -2)

    # Tests for merge_intervals
    def test_merge_intervals_overlapping(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_non_overlapping(self):
        intervals = [[1, 2], [3, 4], [5, 6]]
        expected = [[1, 2], [3, 4], [5, 6]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_unsorted_input(self):
        intervals = [[5, 7], [1, 4], [2, 3]]
        expected = [[1, 4], [5, 7]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_contained(self):
        intervals = [[1, 10], [2, 5], [6, 8]]
        expected = [[1, 10]]
        self.assertEqual(merge_intervals(intervals), expected)

    def test_merge_intervals_rare_case(self):
        intervals = [[1, 4], [100, 400], [3, 101]]
        expected = [[1, 400]]
        self.assertEqual(merge_intervals(intervals), expected)

    # Tests for has_cycle
    def test_has_cycle_no_cycle(self):
        # 1 -> 2 -> 3 -> None
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n1.next = n2
        n2.next = n3
        self.assertFalse(has_cycle(n1))

    def test_has_cycle_simple_cycle(self):
        # 1 -> 2 -> 3 -> back to 1
        n1 = ListNode(1)
        n2 = ListNode(2)
        n3 = ListNode(3)
        n1.next = n2
        n2.next = n3
        n3.next = n1
        self.assertTrue(has_cycle(n1))

    def test_has_cycle_cycle_at_middle(self):
        # 1 -> 2 -> 3 -> 4 -> back to 2
        nodes = [ListNode(i) for i in range(1, 5)]
        for i in range(3):
            nodes[i].next = nodes[i + 1]
        nodes[3].next = nodes[1]
        self.assertTrue(has_cycle(nodes[0]))

    def test_has_cycle_single_node_no_cycle(self):
        n = ListNode(1)
        self.assertFalse(has_cycle(n))

    def test_has_cycle_single_node_self_cycle(self):
        n = ListNode(1)
        n.next = n
        self.assertTrue(has_cycle(n))


if __name__ == "__main__":
    unittest.main()
