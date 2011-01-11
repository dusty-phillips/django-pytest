def run_tests(test_labels, verbosity=1, interactive=True, extra_tests=[]):
    import sys
    from pkg_resources import load_entry_point
    sys.argv[1:] = sys.argv[2:]

    sys.exit(
       load_entry_point('pytest>=2.0', 'console_scripts', 'py.test')()
    )
