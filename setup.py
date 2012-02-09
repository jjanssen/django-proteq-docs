#!/usr/bin/env python
from setuptools import setup, find_packages


METADATA = dict(
    name='django-proteq-docs',
    version='1.0',

    author='Janneke Janssen',
    author_email='j.janssen@lukkien.com',

    description="""Provides a way to integrate a protected sphinx based
    documentation within your django app.""",
    long_description=open('README.rst').read(),

    url='http://github.com/jjanssen/django-proteq-docs',
    download_url='http://github.com/jjanssen/django-proteq-docs',

    install_requires=[],

    include_package_data=True,

    packages=find_packages(),

    keywords='django documentation authentification',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public \
License (LGPL)',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)

if __name__ == '__main__':
    setup(**METADATA)
