#
#
# def testProc(n=[]):
#     pass
# # Do something with n
# testProc([1, 2, 3])  # Explicitly passing in a list
# testProc()  # Using a default empty list
# ##Added line for nitesh2

# def abc():
#     a = 10
#     #return False if a == 10 else True
#     return (False, True) [a == 11]
#
#
# def bcd():
#     a = 10
#     return a == 11
# print(bcd())


import inspect
class Garbage:


    def __init__(self) -> None:
        attrs = (getattr(self, name) for name in dir(self))
        methods = filter(inspect.ismethod, attrs)
        print(methods)
        for method in methods:
            if method.__name__ != '__init__':
                print(method.__name__)
                setattr(self, method.__name__, lambda *args, **kwargs: None)
                #print(getattr(self,method.__name__))

#
# class BCD(metaclass=ABCMeta):
#     @abstractmethod
#     def method2(self):
#         return NotImplementedError

class BCD:
    def __init__(self):
        pass
    def test(self):
        return 10


class ABC(BCD, Garbage):


    def __init__(self):
        self.data = "13"
        self.var2 = "1234"
        BCD.__init__(self)
        Garbage.__init__(self)

    def meth(self):
        pass


obj = ABC()
#obj.meth()
print("**********", obj.test())

# def abc(a):
#     print(a)
#
# a = 10
# abc(a or 2)


