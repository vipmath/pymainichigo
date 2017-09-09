from os import path
from setuptools import setup, find_packages  # Always prefer setuptools over distutils


here = path.abspath(path.dirname(__file__))

setup(
    name='pymainichigo',
    version='1.0.0',

    description='Wallpaper generator for Go/Baduk/Weiqi positions',
    long_description='Generates and sets your wallpaper to a daily Go game, ' +
                     'with each move spaced out over the course of a whole day',

    url='https://github.com/apetresc/pymainichigo',

    author='Adrian Petrescu',
    author_email='apetresc@gmail.com',

    license='GPL',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
    ],

    packages=find_packages(exclude=['test*']),

    install_requires=[
        'sgf==0.5',
        'pyyaml==3.12',
        'xvfbwrapper==0.2.9',
        'Jinja2==2.9.6'
    ],

    package_data={ 'pymainichigo': ['goban.pde.template', 'test.sgf'] },

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={ 'console_scripts': [ 'sample=sample:main', ], },
    entry_points={
        "console_scripts": [
            'pymainichigo=pymainichigo.main:main'
            ]
    },
)
