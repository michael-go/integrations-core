# (C) Datadog, Inc. 2018
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from setuptools import setup, find_packages
from codecs import open  # To use a consistent encoding
from os import path


HERE = path.abspath(path.dirname(__file__))

ABOUT = {}
with open(path.join(HERE, "datadog_checks", "__about__.py")) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
LONG_DESC = ""
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESC = f.read()

setup(
    # Version should always match one from an agent release
    version=ABOUT["__version__"],

    name='datadog_checks_base',
    description='The Datadog Check Toolkit',
    long_description=LONG_DESC,
    keywords='datadog agent checks',
    url='https://github.com/DataDog/datadog-agent-tk',
    author='Datadog',
    author_email='packages@datadoghq.com',
    license='New BSD',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    packages=find_packages(),

    setup_requires=['pytest-runner',],
    tests_require=['pytest<4',],
    install_requires=[
        # 'requests==2.11.1',
        # 'pyyaml==3.11',
        # 'simplejson==3.6.5',
        # 'docker-py==1.10.6',
        # 'python-etcd==0.4.5',
        # 'python-consul==0.4.7',
        # 'kazoo==2.2.1',
    ],
)
