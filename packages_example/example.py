from packages import *
# According to __init__.py,
# [module1, module2, submodules] are imported

module1.module1_foo()
module2.module2_foo()

# Modules inside submodules is not automatically imported
# According to __init__.py,
# [module3, module4] are imported
## prefix 'packages' is still needed
from packages.submodules import *

module3.module3_foo()
module4.module4_foo()
