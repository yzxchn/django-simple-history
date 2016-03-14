import shutil

from django.conf import settings


def pytest_configure():
    shutil.rmtree(settings.MEDIA_ROOT, ignore_errors=True)
