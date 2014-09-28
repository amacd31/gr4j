import os
from io import open

import versioneer
versioneer.versionfile_source = 'gr4j/_version.py'
versioneer.versionfile_build = 'gr4j/_version.py'
versioneer.tag_prefix = 'v'
versioneer.parentdir_prefix = 'gr4j-'

from setuptools import setup
try:
    from Cython.Build import cythonize
    ext_modules = cythonize(["gr4j/gr4j.py"])
except:
    ext_modules = []

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygr4j',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Pure Python implementation of the GR4J hydrologic rainfall-runoff model.',
    long_description=long_description,
    author='Andrew MacDonald',
    author_email='andrew@maccas.net',
    license='BSD',
    url='https://github.com/amacd31/pygr4j',
    packages = ['gr4j'],
    ext_modules = ext_modules,
    test_suite = 'tests',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: BSD License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
