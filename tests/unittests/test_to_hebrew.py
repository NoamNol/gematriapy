import unittest
import gematriapy


class TestGematriapy_ToHebrew(unittest.TestCase):
    def test_simple_num(self):
        self.assertEqual(gematriapy.to_hebrew(3), "ג")

    def test_15_num(self):
        """
        A special case where it's traditional to replace the letters
        for 10 + 5 with letters for 9 + 6.
        """
        self.assertEqual(gematriapy.to_hebrew(15), "טו")

    def test_16_num(self):
        """
        A special case where it's traditional to replace the letters
        for 10 + 6 with letters for 9 + 7.
        """
        self.assertEqual(gematriapy.to_hebrew(16), "טז")

    def test_random_tens_num_v1(self):
        self.assertEqual(gematriapy.to_hebrew(24), "כד")

    def test_random_tens_num_v2(self):
        self.assertEqual(gematriapy.to_hebrew(77), "עז")

    def test_random_hundreds_num_v1(self):
        self.assertEqual(gematriapy.to_hebrew(250), "רנ")

    def test_random_hundreds_num_v2(self):
        self.assertEqual(gematriapy.to_hebrew(499), "תצט")

    def test_random_hundreds_num_v3(self):
        self.assertEqual(gematriapy.to_hebrew(766), "תשסו")

    def test_bigger_than_800_num(self):
        self.assertEqual(gematriapy.to_hebrew(822), "תתכב")

    def test_hundreds_num_that_ends_with_15(self):
        self.assertEqual(gematriapy.to_hebrew(515), "תקטו")

    def test_hundreds_num_that_ends_with_16(self):
        self.assertEqual(gematriapy.to_hebrew(516), "תקטז")

    def test_zero(self):
        with self.assertRaises(ValueError):
            gematriapy.to_hebrew(0)

    def test_zero_with_add_gershayim(self):
        with self.assertRaises(ValueError):
            gematriapy.to_hebrew(0, add_gershayim=True)

    def test_negative(self):
        with self.assertRaises(ValueError):
            gematriapy.to_hebrew(-1)

    def test_too_big(self):
        with self.assertRaises(ValueError):
            gematriapy.to_hebrew(1000)

    def test_add_gershayim_one_letter(self):
        self.assertEqual(gematriapy.to_hebrew(3, add_gershayim=True), 'ג׳')

    def test_add_gershayim_two_letters(self):
        self.assertEqual(gematriapy.to_hebrew(13, add_gershayim=True), 'י״ג')

    def test_add_gershayim_two_letters_value_16_and_17(self):
        """
        15 and 16 are a special case in Hebrew.
        """
        self.assertEqual(gematriapy.to_hebrew(15, add_gershayim=True), 'ט״ו')
        self.assertEqual(gematriapy.to_hebrew(16, add_gershayim=True), 'ט״ז')

    def test_add_gershayim_three_letters(self):
        self.assertEqual(gematriapy.to_hebrew(115, add_gershayim=True), "קט״ו")

    def test_add_gershayim_four_letters(self):
        self.assertEqual(gematriapy.to_hebrew(766, add_gershayim=True), "תשס״ו")
