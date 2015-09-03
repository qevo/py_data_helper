"""Tests for the data_helper.check module"""

import sys, unittest
from BaseTest import BaseTestWrapper

class IsBoolTestCase(BaseTestWrapper.BaseTest):
    """check.is_bool() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_number(self):
        """Test if a number is False"""

        x = 12345
        self.assertFalse(self._bt['func'](x))

    def test_list(self):
        """Test if a list is False"""

        x = []
        self.assertFalse(self._bt['func'](x))

    def test_bool(self):
        """Test if a bool is True"""

        x = True
        self.assertTrue(self._bt['func'](x))


class IsStrTestCase(BaseTestWrapper.BaseTest):
    """check.is_str() test cases"""

    def test_string(self):
        """Test if string is True"""

        x = 'y'
        self.assertTrue(self._bt['func'](x))

    def test_number(self):
        """Test if a number is False"""

        x = 12345
        self.assertFalse(self._bt['func'](x))

    def test_list(self):
        """Test if a list is False"""

        x = []
        self.assertFalse(self._bt['func'](x))


class IsStrEmptyTestCase(BaseTestWrapper.BaseTest):
    """check.is_str_empty() test cases"""

    def test_empty_string(self):
        """Test if an empty string is True"""

        x = ''
        self.assertTrue(self._bt['func'](x))

    def test_string(self):
        """Test if non empty string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_number(self):
        """Test if a number is False"""

        x = 12345
        self.assertFalse(self._bt['func'](x))

    def test_list(self):
        """Test if a list is False"""

        x = []
        self.assertFalse(self._bt['func'](x))


class IsStrNotEmptyTestCase(BaseTestWrapper.BaseTest):
    """check.is_str_not_empty() test cases"""

    def test_empty_string(self):
        """Test if an empty string is False"""

        x = ''
        self.assertFalse(self._bt['func'](x))

    def test_string(self):
        """Test if non empty string is True"""

        x = 'y'
        self.assertTrue(self._bt['func'](x))

    def test_number(self):
        """Test if a number is False"""

        x = 12345
        self.assertFalse(self._bt['func'](x))

    def test_list(self):
        """Test if a list is False"""

        x = []
        self.assertFalse(self._bt['func'](x))


class IsIntTestCase(BaseTestWrapper.BaseTest):
    """check.is_int() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_positive_int(self):
        """Test if a positive int is detected"""

        x = 12345
        self.assertTrue(self._bt['func'](x))

    def test_negative_int(self):
        """Test if a negative int is detected"""

        x = -12345
        self.assertTrue(self._bt['func'](x))


class IsIntNotNegTestCase(BaseTestWrapper.BaseTest):
    """check.is_int_not_neg() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_positive_int(self):
        """Test if a positive int is detected"""

        x = 12345
        self.assertTrue(self._bt['func'](x))

    def test_zero(self):
        """Test if zero is detected"""

        x = 0
        self.assertTrue(self._bt['func'](x))

    def test_negative_int(self):
        """Test if a negative int is detected"""

        x = -12345
        self.assertFalse(self._bt['func'](x))


class IsIntPosTestCase(BaseTestWrapper.BaseTest):
    """check.is_int_pos() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_positive_int(self):
        """Test if a positive int is detected"""

        x = 12345
        self.assertTrue(self._bt['func'](x))

    def test_zero(self):
        """Test if zero is detected"""

        x = 0
        self.assertFalse(self._bt['func'](x))

    def test_negative_int(self):
        """Test if a negative int is detected"""

        x = -12345
        self.assertFalse(self._bt['func'](x))


class IsIntNegTestCase(BaseTestWrapper.BaseTest):
    """check.is_int_pos() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_positive_int(self):
        """Test if a positive int is detected"""

        x = 12345
        self.assertFalse(self._bt['func'](x))

    def test_zero(self):
        """Test if zero is detected"""

        x = 0
        self.assertFalse(self._bt['func'](x))

    def test_negative_int(self):
        """Test if a negative int is detected"""

        x = -12345
        self.assertTrue(self._bt['func'](x))


class IsListTestCase(BaseTestWrapper.BaseTest):
    """check.is_list() test cases"""

    def test_string(self):
        """Test if string is False"""

        x = 'y'
        self.assertFalse(self._bt['func'](x))

    def test_dict(self):
        """Test if dict is False"""

        x = {}
        self.assertFalse(self._bt['func'](x))

    def test_list(self):
        """Test if list is True"""

        x = []
        self.assertTrue(self._bt['func'](x))


class HasWhitespaceTestCase(BaseTestWrapper.BaseTest):
    """check.has_whitespace() test cases"""

    def test_space(self):
        """Test if whitespace is detected"""

        l = [
            'hello world',
            '  ',
            ' space'
        ]
        for s in l:
            self.assertTrue(self._bt['func'](s))

    def test_no_space(self):
        """Test if no whitespace is detected"""
        l = [
            'hello',
            '',
            'none'
        ]
        for s in l:
            self.assertFalse(self._bt['func'](s))


if __name__ == '__main__':
    unittest.main(sys.modules[__name__])
else:
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])