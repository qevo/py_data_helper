"""Command line package entry point"""

from sys import argv
from SuiteHandler import SuiteHandler


if __name__ == "__main__":
    try:
        mod_name  = argv[1]
    except:
        mod_name = "_"

    sh = SuiteHandler()
    sh.run_suite(mod_name)
    print sh.result
