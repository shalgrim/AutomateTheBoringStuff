from unittest import TestCase
from spreadsheet_to_text_files import strip_blank_lines


class TestStrip_blank_lines(TestCase):
    def test_strip_blank_lines_none(self):
        """no blank lines at the end of the list"""
        orig_list = ['a', 'b']
        self.assertEqual(strip_blank_lines(orig_list), [])

    def test_strip_blank_lines_all(self):
        """all blank lines"""
        inlist = [' ', '    ', '']
        outlist = []
        self.assertEqual(strip_blank_lines(inlist), outlist)

    def test_strip_blank_lines_one(self):
        """one blank line"""
        inlist = ['not a blank line', '']
        self.assertEqual(strip_blank_lines(inlist), inlist[:1])

    def test_strip_blank_lines_two(self):
        """two blank lines"""
        inlist = ['not a blank line', '', '\t']
        self.assertEqual(strip_blank_lines(inlist), inlist[:2])
