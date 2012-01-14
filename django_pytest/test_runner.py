class TestRunner(object):
    def __init__(self, verbosity=1, interactive=True, failfast=True, **kwargs):
        self.verbosity = verbosity
        self.interactive = interactive
        self.failfast = failfast

    def run_tests(self, test_labels, extra_tests=None):
        import pytest
        import sys

        if test_labels is None:
            print ('Not yet implemented: py.test is still not able to '
                   'discover the tests in all the INSTALLED_APPS as Django '
                   'requires.')
            exit(1)

        if extra_tests:
            print ('Not yet implemented: py.test is still not able to '
                   'run extra_tests as Django requires.')
            exit(1)

        pytest_args = []
        if self.failfast:
            pytest_args.append('--exitfirst')
        if self.verbosity == 0:
            pytest_args.append('--quiet')
        elif self.verbosity > 1:
            pytest_args.append('--verbose')

        # Remove arguments before (--). This separates Django command options
        # from py.test ones.
        try:
            pytest_args_index = sys.argv.index('--') + 1
            pytest_args.extend(sys.argv[pytest_args_index:])
        except ValueError:
            pass

        sys.exit(pytest.main(pytest_args))


# Keep the old name to be backwards-compatible
def run_tests(test_labels, verbosity=1, interactive=True, extra_tests=None):
    runner = TestRunner(verbosity, interactive, failfast=False)
    runner.run_tests(test_labels, extra_tests)
