import unittest

from src.bubble_sort import BubbleSort


class BubbleSortTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sorter = BubbleSort()

    def setUp(self):
        self.sut = self.sorter

    def tearDown(self):
        self.sut = None

    def test_cp1_empty_list(self):
        vet = []
        result = self.sut.sort(vet)
        self.assertEqual([], result)

    def test_cp1_single_element(self):
        vet = [7]
        result = self.sut.sort(vet)
        self.assertEqual([7], result)

    def test_cp2_already_sorted(self):
        vet = [1, 2]
        result = self.sut.sort(vet)
        self.assertEqual([1, 2], result)

    def test_cp3_single_swap(self):
        vet = [2, 1]
        result = self.sut.sort(vet)
        self.assertEqual([1, 2], result)

    def test_cp4_multiple_passes_with_swaps(self):
        vet = [3, 1, 2]
        result = self.sut.sort(vet)
        self.assertEqual([1, 2, 3], result)

    def test_reverse_order(self):
        vet = [5, 4, 3, 2, 1]
        result = self.sut.sort(vet)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_repeated_values(self):
        vet = [4, 2, 4, 1, 2]
        result = self.sut.sort(vet)
        self.assertEqual([1, 2, 2, 4, 4], result)

    def test_negative_values(self):
        vet = [0, -3, 5, -1]
        result = self.sut.sort(vet)
        self.assertEqual([-3, -1, 0, 5], result)

    def test_sorts_in_place(self):
        vet = [3, 2, 1]
        result = self.sut.sort(vet)
        self.assertIs(vet, result)


if __name__ == "__main__":
    unittest.main()
