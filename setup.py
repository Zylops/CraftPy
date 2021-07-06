from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

VERSION = '1.1.3'
DESCRIPTION = 'Controlling minecraft with python'
LONG_DESCRIPTION = open('README.md', 'r').read()

# Setting up
setup(
    name="CraftPy",
    version=VERSION,
    author="Zylops",
    author_email="zainaazeez787@gmail.com",
    description=DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires=['pyautogui'],
    keywords=['python', 'gaming', 'mc', 'control', 'pyautogui', 'minecraft'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
