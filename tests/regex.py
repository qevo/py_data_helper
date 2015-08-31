"""Tests for the data_helper.regex module"""

from BaseTest import BaseTestWrapper, do_main


class WildcardReTestCase(BaseTestWrapper.BaseTest):
    """regex.wildcard_re() test cases"""

    def test_alpha_pattern(self):
        """Test if a string with only alpha characters returns with the same value"""

        string = 'abcdefghijklm'
        result = self._bt['func'](string)
        self.assertEqual(string, result)

    def test_alphanum_pattern(self):
        """Test if a string with only alphanumeric characters returns with the same value"""

        string = 'abcdefghijklm12345'
        result = self._bt['func'](string)
        self.assertEqual(string, result)

    def test_wildcard(self):
        """Test if a string with a wildcard character returns with the correct modification"""

        string = 'foo*bar'
        result = self._bt['func'](string)
        self.assertEqual(result, 'foo.*bar')

    def test_punctuation(self):
        """Test if a string with a punctuation character returns with the correct modification"""

        string = 'foo?bar'
        result = self._bt['func'](string)
        self.assertEqual(result, 'foo\\?bar')


if __name__ == '__main__':
    do_main()
