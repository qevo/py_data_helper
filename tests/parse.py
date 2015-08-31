"""Tests for the data_helper.parse module"""

import sys, unittest
from re import IGNORECASE
from BaseTest import BaseTestWrapper, do_main

class StrSplitSizeTestCase(BaseTestWrapper.BaseTest):
    """parse.str_split_size() test cases"""

    def test_concat_string(self):
        """Test if a string concatenated N times is split N times"""

        string = 'abcdabcdabcd'
        n = 5
        i = 0
        concat_str = ''
        while i < n:
            concat_str += string
            i += 1
        result = self._bt['func'](concat_str, len(string))
        self.assertEqual(n, len(result))
        self.assertEqual(''.join(result), concat_str)

    def test_even_length_string(self):
        """Test the value and number of elements returned from a string whose length is an even number"""

        string = 'abcdabcdabcd'
        length = len(string)
        result = self._bt['func'](string, 2)
        self.assertEqual(length / 2, len(result))
        self.assertEqual(''.join(result), string)

    def test_odd_length_string(self):
        """Test the value and number of elements returned from a string whose length is an odd number"""

        string = 'abcabcabc'
        length = len(string)
        result = self._bt['func'](string, 2)
        self.assertEqual((length / 2) + 1, len(result))
        self.assertEqual(''.join(result), string)

    def test_integer(self):
        """Test the value and number of elements returned from an integer"""

        integer = 1010101010
        length = len(str(integer))
        result = self._bt['func'](integer, 2)
        self.assertEqual(length / 2, len(result))
        self.assertEqual(''.join(result), str(integer))


class StrSplitCapsTestCase(BaseTestWrapper.BaseTest):
    """parse.str_split_caps() test cases"""

    def test_trim(self):
        """Test if whitespace is trimmed"""

        string = 'Foo  Bar'
        result = self._bt['func'](string, False)
        self.assertListEqual(result, ['Foo  ', 'Bar'])
        result = self._bt['func'](string, True)
        self.assertListEqual(result, ['Foo', 'Bar'])


class ListFilterTestCase(BaseTestWrapper.BaseTest):
    """parse.list_filter() test cases"""

    @classmethod
    def setUpClass(self):
        cls = self.__mro__[0]
        super(cls, self).setUpClass()

        self._bt['sample_list'] = [
            'abcdefghijklm',
            'NOPQRSTUVWXYZ',
            'example.txt',
            './readme.md',
            '1234567890',
            'hello world',
            '123 Fake St.'
        ]

    def test_wildcard(self):
        """Test if a pattern matching any characters returns all"""

        p = '.*'
        l = self._bt['sample_list']
        result = self._bt['func'](p, l)
        self.assertListEqual(result, l)

    def test_file_ext(self):
        """Test a pattern for matching a file extension '.md'"""

        p = '^.*\.md$'
        l = self._bt['sample_list']
        result = self._bt['func'](p, l)
        self.assertListEqual(result, ['./readme.md'])

    def test_case_i(self):
        """Test a case insensitive pattern"""

        p = '^[a-z]+$'
        l = self._bt['sample_list']
        result = self._bt['func'](p, l, IGNORECASE)
        self.assertListEqual(result, ['abcdefghijklm', 'NOPQRSTUVWXYZ'])

    def test_caps_only(self):
        """Test a pattern for only capital letters"""

        p = '^[A-Z]+$'
        l = self._bt['sample_list']
        result = self._bt['func'](p, l)
        self.assertListEqual(result, ['NOPQRSTUVWXYZ'])

    def test_has_numbers(self):
        """Test a pattern for numbers included"""

        p = '^.*[0-9]+.*$'
        l = self._bt['sample_list']
        result = self._bt['func'](p, l)
        self.assertListEqual(result, ['1234567890', '123 Fake St.'])


def run_mod_tests():
    do_main(sys.modules[__name__])

if __name__ == '__main__':
    do_main(sys.modules[__name__])
else:
    suite = unittest.defaultTestLoader.suiteClass
