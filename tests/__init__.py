"""data_helper tests package"""

from SuiteHandler import SuiteHandler


def run(sh, *args):
    sh.run_suite(*args)


sh = SuiteHandler()

if __name__ == "__main__":
    run(sh)
    print sh.result
