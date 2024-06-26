from setuptools import setup

setup(
   name='dialogue',
   version='1.0',
   description='Module for parsing JSON dialogue data.',
   author='Michael Maddin, Marina Montgomery',
   author_email='foomail@foo.example',
   packages=['dialogue'],  #same as name
   install_requires=['wheel', 'bar', 'greek'], #external packages as dependencies
   scripts=[
            'scripts/cool',
            'scripts/skype',
           ]
)