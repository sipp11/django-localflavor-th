import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name = 'django-localflavor-th',
    version = '0.1',
    description = 'Country-specific Django helpers for Thailand',
    long_description = README,
    author = 'sipp11',
    author_email = 'sipp11@mycapsules.com',
    license='BSD',
    url = 'https://github.com/sipp11/django-localflavor-th',
    packages = ['django_localflavor_th'],
    include_package_data = True,
    classifiers = [
        'Development Status :: 1 - Planning',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=[
        'Django>=1.4',
    ]
)
