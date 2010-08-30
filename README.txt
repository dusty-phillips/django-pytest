django-pytest
=============

This project allows you to use py.test as a django test runner, instead of the
default test runner.

To use it, add it to your python path and add *django_pytest* to your installed
apps. Also set the *TEST_RUNNER = 'django_pytest.test_runner.run_tests'* setting.

Also create a conftest.py in your project directory and include:
from django_pytest.conftest import pytest_funcarg__client, pytest_funcarg__django_client

You can also use
from django_pytest.auth_funcargs import pytest_funcarg__user, pytest_funcarg__groups

to import a user or some groups with users in them

Now anywhere in your project, you can create files called
*test_<something>.py*.  These are standard py.test test files. Use the funcarg
*client* in every test to both instantiate a test database that is cleared
after each test and to provide you with a django test client object identical
to the one used in django's test system. For example:

def test_filter(client):
    response = client.get('/browse/', {'filter': '1'})
    assert response.status_code == 200

Use *./manage.py test* to run the py.test test runs (ie: it replaces the
standard django test runner). You can pass py.test options to the command
and they will be forwarded to py.test. (Technically, I haven't got it passing
all options, just the most common ones I use)

The management command has been set up so that syncdb will use the django core
syncdb if SOUTH_TESTS_MIGRATE is set to False, if south is installed. This
prevents migrations from running when running unit tests. This speeds up test
setup significantly, but it means your test db may not be identical to
production, if you have faulty migrations.

py.test automatically picks up any subclasses of unittest.TestCase, provided
they are in a module named test_<something>.py. Thus, all your existing django
unittests should work seemlessly with py.test, although you may have to rename
your test files if they do not conform to this convention. You can also write
custom py.test test collection hooks to pick up test modules that are named in
a different directory structure.

This project differs from http://github.com/bfirsh/pytest_django in that it
provides a django test runner that calls py.test, rather than creating a
py.test plugin to test django projects. I believe there is overlapping
functionality from the two projects, and also that they can be integrated into
a single project, but I have not looked at the feasibility of this yet.
