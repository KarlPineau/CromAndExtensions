from setuptools import setup
import sys

if (sys.version_info[0:2] < (2,7)):
    install_requires =['ordereddict', 'future']
else:
    install_requires = []

setup(
    name = 'CromAndExtensions',
    packages = ['CromAndExtensions'],
    package_data = {
        'CromAndExtensions': ['data/crm_vocab.tsv', 'data/overrides.json',
        'data/key_order.json', 'data/linked-art.json', 
        'data/cidoc-extension.json', 'data/crm-profile.json']
    },
    test_suite="tests",
    version = '0.1',
    description = 'Mapping CIDOC-CRM classes & extensions to Python objects',
    author = 'Karl Pineau, fork Rob Sanderson',
    author_email = 'karl.pineau@utc.fr',
    url = '',
    install_requires=install_requires,
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: Apache Software License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
