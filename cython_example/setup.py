'''Use this setup code
- to generate code from Cython to C-extensions for Python
'''
from distutils.core import setup
from Cython.Build import cythonize
setup(ext_modules = cythonize('fastfac.pyx'))