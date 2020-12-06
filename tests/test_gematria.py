import unittest
from gematriapy import Gematria


class Test_Gematria(unittest.TestCase):
    gematria = Gematria()

    def test_simple_num(self):
        self.assertEqual(self.gematria.number_to_hebrew(3), "ג")

    def test_15_num(self):
        self.assertEqual(self.gematria.number_to_hebrew(15), "טו")

    def test_16_num(self):
        self.assertEqual(self.gematria.number_to_hebrew(16), "טז")

    def test_random_tens_num_v1(self):
        self.assertEqual(self.gematria.number_to_hebrew(24), "כד")

    def test_random_tens_num_v2(self):
        self.assertEqual(self.gematria.number_to_hebrew(77), "עז")

    def test_random_hundreds_num_v1(self):
        self.assertEqual(self.gematria.number_to_hebrew(250), "רנ")

    def test_random_hundreds_num_v2(self):
        self.assertEqual(self.gematria.number_to_hebrew(499), "תצט")

    def test_bigger_than_800_num(self):
        self.assertEqual(self.gematria.number_to_hebrew(822), "תתכב")

    def test_hundreds_num_that_ends_with_15(self):
        self.assertEqual(self.gematria.number_to_hebrew(515), "תקטו")

    def test_hundreds_num_that_ends_with_16(self):
        self.assertEqual(self.gematria.number_to_hebrew(416), "תקטז")

    def test_zero(self):
        with self.assertRaises(Exception):
            self.gematria.number_to_hebrew(0)

    def test_negative(self):
        with self.assertRaises(Exception):
            self.gematria.number_to_hebrew(-1)

    def test_too_big(self):
        with self.assertRaises(Exception):
            self.gematria.number_to_hebrew(1000)
