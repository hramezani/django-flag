from setuptools import find_packages, setup

VERSION = "0.2.dev10"
LONG_DESCRIPTION = """
.. image:: http://pinaxproject.com/pinax-design/patches/pinax-flag.svg
    :target: https://pypi.python.org/pypi/pinax-flag/

==========
Pinax Flag
==========

.. image:: https://img.shields.io/pypi/v/pinax-flag.svg
    :target: https://pypi.python.org/pypi/pinax-flag/

\

.. image:: https://img.shields.io/circleci/project/github/pinax/pinax-flag.svg
    :target: https://circleci.com/gh/pinax/pinax-flag
.. image:: https://img.shields.io/codecov/c/github/pinax/pinax-flag.svg
    :target: https://codecov.io/gh/pinax/pinax-flag
.. image:: https://img.shields.io/github/contributors/pinax/pinax-flag.svg
    :target: https://github.com/pinax/pinax-flag/graphs/contributors
.. image:: https://img.shields.io/github/issues-pr/pinax/pinax-flag.svg
    :target: https://github.com/pinax/pinax-flag/pulls
.. image:: https://img.shields.io/github/issues-pr-closed/pinax/pinax-flag.svg
    :target: https://github.com/pinax/pinax-flag/pulls?q=is%3Apr+is%3Aclosed

\

.. image:: http://slack.pinaxproject.com/badge.svg
    :target: http://slack.pinaxproject.com/
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://opensource.org/licenses/MIT/

\

``pinax-flag`` is a flaging app for the Django web framework.

``pinax-flag`` provides flagging of inapproprite spam/content.

Supported Django and Python Versions
------------------------------------

+-----------------+-----+-----+-----+-----+
| Django / Python | 2.7 | 3.4 | 3.5 | 3.6 |
+=================+=====+=====+=====+=====+
|  1.11           |  *  |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
|  2.0            |     |  *  |  *  |  *  |
+-----------------+-----+-----+-----+-----+
"""

setup(
    author="Pinax Team",
    author_email="team@pinaxproject.com",
    description="Flagging of inapproprite spam/content for the Django web framework",
    name="pinax-flag",
    long_description=LONG_DESCRIPTION,
    version=VERSION,
    url="http://github.com/pinax/pinax-flag/",
    license="MIT",
    packages=find_packages(),
    package_data={
        "flag": []
    },
    install_requires=[
    ],
    tests_require=[
    ],
    test_suite="runtests.runtests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    zip_safe=False
)
