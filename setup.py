from setuptools import setup, find_packages
from os import path


setup(
    name="django-celsius",
    version='0.0.1',

    description='Application metrics for Django.',
    long_description='Application metrics for Django.',

    url='https://github.com/loftylabs/django-celsius',

    author='Lofty Labs',
    author_email='casey@hirelofty.com',

    license = 'MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        
        # TODO: Test with tox and indicate other supported versions here
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='django analytics metrics',

    packages=find_packages(exclude=['tests*']),
    install_requires=[]
)
