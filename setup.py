#! /usr/bin/env python

import setuptools
import simple_history

setuptools.setup(
    name='django-simple-history',
    version=simple_history.__version__,
    description='Store model history and view/revert changes from admin site.',
    long_description='\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    author='Corey Bertram',
    author_email='corey@qr7.com',
    maintainer='Trey Hunner',
    url='https://github.com/treyhunner/django-simple-history',
    packages=setuptools.find_packages(exclude=[
        'tests',
        'tests.*',
    ]),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "License :: OSI Approved :: BSD License",
    ],
    setup_requires=['pytest-runner'],
    tests_require=[
        'Django>=1.6',
        'django-webtest==1.7.8',
        'mock==1.0.1',
        'pytest',
        'pytest-django',
        'WebTest==2.0.18',
    ],
    include_package_data=True,
)
