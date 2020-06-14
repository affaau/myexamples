''' after defining __all__, calling command
>>> from packages.submodules import *
'module3', 'module4' will be imported
otherwise, nothing is imported
'''
__all__ = ['module3', 'module4']