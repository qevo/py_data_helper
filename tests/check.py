"""Tests for the data_helper.check module"""

from BaseTest import BaseTestWrapper, do_main


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


class IsStrTestCase(BaseTestWrapper.BaseTest):
    """check.is_int() test cases"""

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


if __name__ == '__main__':
    do_main()
