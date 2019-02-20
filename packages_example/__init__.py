''' after defining __all__, calling command
>>> from packages import *
'module1', 'module2', 'submodules' will be imported
otherwise, nothing is imported

After this, assuming __init__.py inside submodules has 
defined __all__, then calling
>>> from submodules import *
'module3', 'module4' will be imported
'''
__all__ = ['module1', 'module2', 'submodules']