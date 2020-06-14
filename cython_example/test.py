'''
To compare speed of C-extension for Python with native Python
'''
from fastfac import fastfactorial
from fac import factorial
from timeit import timeit


print(timeit('fastfactorial(20)', globals=globals(), number=10000))
# 0.0010236000000000134
## 27.4 times faster!

print(timeit('factorial(20)', globals=globals(), number=10000))
# 0.0280349



print(timeit('fastfactorial(120)', globals=globals(), number=10000))
# 0.0036939
## 47 times faster!

print(timeit('factorial(120)', globals=globals(), number=10000))
# 0.1742548
