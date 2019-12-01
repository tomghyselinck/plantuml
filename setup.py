# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.rst') as fh:
    long_desc = fh.read()

requires = ['Sphinx>=1.1']

setup(
    name='sphinxcontrib-plantuml',
    version='0.17.1',
    url='https://github.com/sphinx-contrib/plantuml/',
    download_url='https://pypi.python.org/pypi/sphinxcontrib-plantuml',
    license='BSD',
    author='Yuya Nishihara',
    author_email='yuya@tcha.org',
    description='Sphinx "plantuml" extension',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    extras_require={
        'server': [
            'plantuml',
        ],
    },
    namespace_packages=['sphinxcontrib'],
)
