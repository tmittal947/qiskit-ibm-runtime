# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

import os

from setuptools import setup

requirements = [
    "qiskit-terra>=0.7,<0.8",
    "requests>=2.19",
    "requests-ntlm>=1.1.0",
]

# Handle version.
VERSION_PATH = os.path.join(os.path.dirname(__file__),
                            "qiskit", "providers", "aer", "VERSION.txt")
with open(VERSION_PATH, "r") as version_file:
    VERSION = version_file.read().strip()

setup(
    name="qiskit-ibmq-provider",
    version=VERSION,
    description="Qiskit provider for IBMQ network",
    long_description="Qiskit provider for accessing the IBMQ network, allowing "
                     "access to real quantum devices and simulators.",
    url="https://github.com/Qiskit/qiskit-ibmq-provider",
    author="Qiskit Development Team",
    author_email="qiskit@us.ibm.com",
    license="Apache 2.0",
    classifiers=[
        "Environment :: Console",
        "License :: OSI Approved :: Apache Software License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering",
    ],
    keywords="qiskit sdk quantum api ibmq",
    packages=['qiskit.providers.ibmq'],
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.5"
)