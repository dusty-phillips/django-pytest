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
        make_option('-x', action='store_true', dest='', default=False,
            help='exit instantly on first error or failed test.'),
        make_option('--pdb', action='store_false', dest='pdb', default=False,
            help='Start the python debugger on errors'),
    )

    def run_from_argv(self, argv):
        # Separate Django command options from py.test ones with -- to ensure
        # that Django is not complaining about unknown options.
        try:
            args = argv[:argv.index('--')]
            super(Command, self).run_from_argv(args)
        except ValueError:
            super(Command, self).run_from_argv(argv)

    def handle(self, *args, **kwargs):
        management.get_commands()

        # If south is installed Check if SOUTH_TESTS_MIGRATE is set
        # if it is, use a sync and migrate paradigm
        # if it is not set, use the core command
        # if south is not installed, use default syncdb
        if "south" in settings.INSTALLED_APPS:
            if hasattr(settings, "SOUTH_TESTS_MIGRATE") and not settings.SOUTH_TESTS_MIGRATE:
                management._commands['syncdb'] = 'django.core'
            else:
                from south.management.commands.syncdb import Command as SyncDbCommand
                class MigrateAndSyncCommand(SyncDbCommand):
                    option_list = SyncDbCommand.option_list
                    for opt in option_list:
                        if "--migrate" == opt.get_opt_string():
                            opt.default = True
                            break
                management._commands['syncdb'] = MigrateAndSyncCommand()

        super(Command, self).handle(*args, **kwargs)
