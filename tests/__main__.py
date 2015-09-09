"""Command line package entry point"""

from sys import argv
from SuiteHandler import SuiteHandler
import check, hash, parse, regex, transform


if __name__ == "__main__":
    try:
        mod_name  = argv[1]
    except:
        mod_name = "_"

    sh = SuiteHandler({
        "check": check.suite,
        "hash": hash.suite,
        "parse": parse.suite,
        "regex": regex.suite,
        "transform": transform.suite
    })

    sh.run_suite(mod_name)
    print sh.result
    for f in sh.result.failures:
        for t in f:
            print t
        print ''
    for e in sh.result.errors:
        for t in e:
            print t
        print ''
