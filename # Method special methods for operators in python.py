#special methods for operators in python
>>> import re, requests
>>> set(re.findall('__\w+__', requests.get('https://docs.python.org/3/reference/datamodel.html').text))
set(['__abs__',
     ##'__add__',
     '__aenter__',
     '__aexit__',
     '__aiter__',
     '__and__',
     '__anext__',
     '__annotations__',
     '__await__',
     '__bases__',
     '__bool__',
     '__bytes__',
     '__call__',
     '__ceil__',
     '__class__',
     '__class_getitem__',
     '__classcell__',
     '__closure__',
     '__code__',
     '__complex__',
     '__contains__',
     '__defaults__',
     ##'__del__',
     '__delattr__',
     '__delete__',
     '__delitem__',
     '__dict__',
     '__dir__',
     '__divmod__',
     '__doc__',
     '__enter__',
     '__eq__',
     '__exit__',
     '__file__',
     '__float__',
     '__floor__',
     '__floordiv__',
     '__format__',
     '__func__',
     '__future__',
     '__ge__',
     ##'__get__',
     '__getattr__',
     '__getattribute__',
     '__getitem__',
     '__globals__',
     '__gt__',
     '__hash__',
     '__iadd__',
     '__iand__',
     '__ifloordiv__',
     '__ilshift__',
     '__imatmul__',
     '__imod__',
     '__import__',
     '__imul__',
     '__index__',
     ##'__init__',
     '__init_subclass__',
     '__instancecheck__',
     '__int__',
     '__invert__',
     '__ior__',
     '__ipow__',
     '__irshift__',
     '__isub__',
     '__iter__',
     '__itruediv__',
     '__ixor__',
     '__kwdefaults__',
     '__le__',
     '__len__',
     '__length_hint__',
     '__lshift__',
     '__lt__',
     '__matmul__',
     '__missing__',
     '__mod__',
     '__module__',
     '__mro__',
     '__mro_entries__',
     '__mul__',
     '__name__',
     '__ne__',
     '__neg__',
     '__new__',
     '__next__',
     '__objclass__',
     '__or__',
     '__pos__',
     '__pow__',
     '__prepare__',
     '__qualname__',
     '__radd__',
     '__rand__',
     '__rdivmod__',
     '__repr__',
     '__reversed__',
     '__rfloordiv__',
     '__rlshift__',
     '__rmatmul__',
     '__rmod__',
     '__rmul__',
     '__ror__',
     '__round__',
     '__rpow__',
     '__rrshift__',
     '__rshift__',
     '__rsub__',
     '__rtruediv__',
     '__rxor__',
     '__self__',
     ##'__set__',
     '__set_name__',
     '__setattr__',
     '__setitem__',
     '__slots__',
     ##'__str__',
     '__sub__',
     '__subclasscheck__',
     '__traceback__',
     ##'__truediv__',
     '__trunc__',
     '__weakref__',
     '__xor__'])
