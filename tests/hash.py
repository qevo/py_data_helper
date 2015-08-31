"""Tests for the data_helper.hash module"""

import sys, unittest
from BaseTest import BaseTestWrapper, do_main


class Md5TestCase(BaseTestWrapper.BaseTest):
    """hash.md5() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = 'ea63287cb93455c84d98580b301c7739'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


class Sha1TestCase(BaseTestWrapper.BaseTest):
    """hash.sha1() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = '9df46bb4e4aa30e7da0966f6ac299da9062bc887'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


class Sha224TestCase(BaseTestWrapper.BaseTest):
    """hash.sha1() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = '5f30cd548eceac0391ca02785ab4a1655091d6a6bbfdb96564458f44'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


class Sha256TestCase(BaseTestWrapper.BaseTest):
    """hash.sha1() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = '6c884c41add964b697febec384c39534c0e003adaca3b193287bcb7614c4b35c'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


class Sha384TestCase(BaseTestWrapper.BaseTest):
    """hash.sha1() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = 'c4c19b93f2549604f41ffa45accfbcc7c5cef23b6e14871d668a11a164936a7881f36a404a2f5b45eeff8268024caa0a'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


class Sha512TestCase(BaseTestWrapper.BaseTest):
    """hash.sha1() test cases"""

    def test_match(self):
        """Test if the hash matches"""

        string = 'string to be hashed'
        known_hash = 'bc24010c31dc2b7f21c08ab9ff3a53a1f91756ce67e67d4915d9ae6cabe839881a5ead7ecc2fdbc848c1a31a7fae1dea23e7d9b20a6ead78f82b156c44df1a0e'
        result = self._bt['func'](string)
        self.assertEqual(result, known_hash)


def run_mod_tests():
    do_main(sys.modules[__name__])

if __name__ == '__main__':
    do_main(sys.modules[__name__])
else:
    suite = unittest.defaultTestLoader.suiteClass
