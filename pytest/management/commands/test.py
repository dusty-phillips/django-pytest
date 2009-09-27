from django.core import management
from django.core.management.commands import test
from django.core.management.commands import syncdb
from django.conf import settings
from django.core.management.base import BaseCommand
from optparse import make_option


class Command(test.Command):
    option_list = test.Command.option_list + (
        make_option('-k', action='store', dest='keyword', default='',
            help='Tell py.test to filter out tests that don\'t contain keyword'),
        make_option('-s', action='store_false', dest='capture', default=False,
            help='Tell py.test not to capture output. Useful for dropping to ipython shells'),
    )
    def handle(self, *args, **kwargs):
        # Use syncdb instead of migrate to speed up tests
        management.get_commands()
        management._commands['syncdb'] = 'django.core'
        super(Command, self).handle(*args, **kwargs)
