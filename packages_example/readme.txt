Package or subpackage is directory (with __init__.py)
Module is file


|-- packages
|  |-- __init__.py
|  |-- module1.py: module1_foo
|  |-- module2.py: module2_foo
|  |
|  |-- submodules
|    |-- __init__.py
|    |-- module3.py: module3_foo
|    |-- module4.py: module4_foo
|
|--example.py


Usages:
>>> import packages
# Since 'packages' is a just package, not module,
# calling 'packages.module1' has AttributeError
# This command has no meaning.

>>> import packages.module1
# Since 'module1' is a module, its namespace is created.
# Calling 'packages.module1.module1_foo()' now works!
#
>>> from packages import *
# '__init__.py' inside 'packages' is loaded.
# If __all__ = ['module1', 'module2', 'submodules'] is defined in __init__.py,
# these modules and package are defined.
#
# Since 'module1', 'module2' are modules, their namespaces are created.
# Calling 'module1.module1_foo()' now works.
#
# However, 'submodules' is just a package.
# Calling 'submodules.module3.module3_foo()' has AttributeError, no meaning.
#
# To use 'module3' or 'module4' modules, 
# either
>>> import packages.submodules.module3
# Since 'module3' is a module, 
# calling 'packages.submodules.module3.module3_foo()' now works
#
# or
>>> from packages.submodules import *
# '__init__.py' inside 'submodules' is loaded
# If __all__ = ['module3', module4'] is defined in __init__.py,
# calling 'module3.module3_foo()' now works.
#


=======================
Example folders structure to test
__init__.py and
attribute __all__


Test commands:
>>> import packages

>>> from packages import *

>>> from packages.submodules import *

Q. What happen if __all__ is not defined in __init__.py?