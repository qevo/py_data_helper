"""data_helper tests package

Example:
    Run all tests from parent directory::

        python -m tests

    Run module test::

        python -m tests <module>
        python tests/<module.py>

"""

from SuiteHandler import SuiteHandler
import check, hash, parse, regex, transform


def run(sh, *args):
    sh.run_suite(*args)


sh = SuiteHandler({
    "check": check.suite,
    "hash": hash.suite,
    "parse": parse.suite,
    "regex": regex.suite,
    "transform": transform.suite
})

if __name__ == "__main__":
    run(sh)
    print sh.result
    for f in sh.result.failures:
        for t in f:
            print t
        print ''
    for e in sh.result.errors:
        for t in e:
            print t
        print ''
