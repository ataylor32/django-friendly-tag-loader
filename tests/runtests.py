import os.path
import sys

from django.conf import settings
from django.core import management


def runtests():
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    settings_mod = getattr(__import__('testproject.settings'), 'settings')
    management.setup_environ(settings_mod)
    from django.test.utils import get_runner
    try:
        from django.test.simple import DjangoTestSuiteRunner
        run_tests = get_runner(settings)().run_tests
    except ImportError:
        # for Django versions that don't have DjangoTestSuiteRunner
        run_tests = get_runner(settings)
    failures = run_tests(['testproject'], verbosity=1, interactive=True)
    sys.exit(failures)


if __name__ == '__main__':
    runtests()
