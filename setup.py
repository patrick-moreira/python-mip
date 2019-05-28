import setuptools


# read the version number
version_dict = {}
exec(open('mip/constants.py').read(), version_dict)
VERSION = version_dict['VERSION']

with open("README.md", "r") as fh:
    long_descr = fh.read()

setuptools.setup(
    name="mip",
    python_requires='>3.5.0',
    version=VERSION,
    author="Toffolo, T.A.M. and Santos, H.G.",
    author_email="haroldo@ufop.edu.br",
    description="Python tools for Modeling and Solving Mixed-Integer Linear \
    Programs (MIPs)",
    long_description=long_descr,
    long_description_content_type="text/markdown",
    keywords=["Optimization", "Linear Programming",
              "Integer Programming", "Operations Research"],
    url="https://github.com/coin-or/python-mip",
    packages=['mip', 'mip.libraries'],
    package_data={'mip.libraries': ['*', '*.*']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Eclipse Public License",
        "Operating System :: OS Independent",
    ],
)
