"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(

    name='gcp-utility',  # Required
    version='2.0.4',  # Required
    description='GCP utility will give additional custom features over gcs',  # Required
    long_description=long_description,  # Optional
    url='https://github.com/pypa/sampleproject',  # Optional
    author='Manojkumar vadivel',  # Optional
    author_email='manojkumar.vsj@gmail.com',  # Optional
    long_description_content_type="text/markdown",
    python_requires='>=2.6,<3',
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7'
    ],
    keywords='sample setuptools development',  # Optional
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    install_requires=['google-cloud-bigquery==1.24.0', 'Jinja2==2.11.3'],  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },
    package_data={  # Optional
        'sample': ['package_data.dat'],
    },
    data_files=[('my_data', ['data/data_file'])],  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'bq_client=gcputils.bq_client:main',
        ],
    },
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/pypa/sampleproject/issues',
        'Funding': 'https://donate.pypi.org',
        'Say Thanks!': 'http://saythanks.io/to/example',
        'Source': 'https://github.com/pypa/sampleproject/',
    },
)
