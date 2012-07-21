from setuptools import setup

name = 'normalizer'

setup (
        name = name,
        version = '0.1',
        url = 'http://silpa.org.in/',
        license = 'LGPL 3.0',
        description = 'Malayalam language normalizer (Experimental)',
        author = 'Santhosh Thottingal',
        author_email = 'santhosh.thottingal@gmail.com',
        long_description = 'Normalizing module for Malayalam language',
        include_package_data = True,
        setup_requires = ['setuptools-git'],
        install_requires = ['setuptools'],
        zip_safe = False,
        
)
