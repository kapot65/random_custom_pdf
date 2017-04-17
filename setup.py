# -*- coding: utf-8 -*-

from setuptools import setup
from pip.req import parse_requirements

install_reqs = parse_requirements("random_custom_pdf/requirements.txt", 
                                  session='hack')
reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="random_custom_pdf",
    description='numpy based random generator with custom probability '
    'distribution function',
    version="0.0.1",
    author="Vasiliy Chernov",
    author_email='kapot65@gmail.com',
    packages=["random_custom_pdf"],
    platforms='any',
    install_requires=reqs
)