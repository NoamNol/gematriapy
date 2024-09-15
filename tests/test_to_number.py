import unittest
import gematriapy


class TestGematriapy_ToNumber(unittest.TestCase):
    def test_single_letter_to_3(self):
        self.assertEqual(gematriapy.to_number("ג"), 3)

    def test_single_letter_to_9(self):
        self.assertEqual(gematriapy.to_number("ט"), 9)

    def test_long_hebrew_v1(self):
        self.assertEqual(gematriapy.to_number("קכו"), 126)

    def test_long_hebrew_v2(self):
        self.assertEqual(gematriapy.to_number("רטו"), 215)

    def test_long_hebrew_v3(self):
        self.assertEqual(gematriapy.to_number("שלום"), 376)

    def test_single_final_letter(self):
        """
        In Hebrew, 'final' letters are different from regular letters.
        Some letters have a special shape if positioned at the end of a word.
        """
        self.assertEqual(gematriapy.to_number("ך"), 20)
        self.assertEqual(gematriapy.to_number("ם"), 40)
        self.assertEqual(gematriapy.to_number("ן"), 50)
        self.assertEqual(gematriapy.to_number("ף"), 80)
        self.assertEqual(gematriapy.to_number("ץ"), 90)

    def test_illegal_hebrew_number_v1(self):
        """
        In Hebrew, letters representing a numerical value should have an order:
        big numbers come before small numbers.
        So "ת" should come before "י".

        to_number should not care about that and just return the 'gematriapy'
        value - the sum of the numerical value of the letters.
        """
        self.assertEqual(gematriapy.to_number("יתג"), 413)

    def test_illegal_hebrew_number_v2(self):
        self.assertEqual(gematriapy.to_number("אבא"), 4)

    def test_empty(self):
        self.assertEqual(gematriapy.to_number(""), 0)

    def test_non_hebrew(self):
        self.assertEqual(gematriapy.to_number("abc"), 0)

    def test_hebrew_and_non_hebrew(self):
        self.assertEqual(gematriapy.to_number("aאbהc"), 6)

    def test_hebrew_with_nikud(self):
        self.assertEqual(gematriapy.to_number("שלום"), 376)
        self.assertEqual(gematriapy.to_number("שָׁלוֹם"), 376)
