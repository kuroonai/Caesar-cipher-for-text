from setuptools import setup

setup(
   name='kcctext',
   version='1.0',
   description="Kuroonai's Caesar cipher for text"
   author='Naveen Vasudevan',
   author_email='naveenovan@gmail.com',
   packages=['kcctext'],  #same as name
   install_requires=['PySimpleGUI','clipboard'], #external packages as dependencies
)