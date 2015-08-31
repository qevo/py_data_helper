"""Tests for the data_helper.transform module"""

import sys, unittest
from BaseTest import BaseTestWrapper, do_main


class CamelcaseToUnderscoreTestCase(BaseTestWrapper.BaseTest):
    """transform.camelcase_to_underscore() test cases"""

    def test_whitespace(self):
        """Test if a string with whitespace is rejected"""

        string = 'hello world'
        try:
            result = self._bt['func'](string)
        except:
            return True
        return False

    def test_camelcase(self):
        """Test if a CamelCase string is transformed"""

        string = "CamelCase"
        result = self._bt['func'](string)
        self.assertEqual(result, 'camel_case')

    def test_unaffected(self):
        """Test is a string with no whitespace is returned unaltered"""

        string = "word"
        result = self._bt['func'](string)
        self.assertEqual(result, string)


def run_mod_tests():
    do_main(sys.modules[__name__])

if __name__ == '__main__':
    do_main(sys.modules[__name__])
else:
    suite = unittest.defaultTestLoader.suiteClass
