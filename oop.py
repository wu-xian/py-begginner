class BaseClass(object):
    def showA(self):
        print("A")
    
    def showB(self):
        print("B")

    # predefined
    def __showC(self):
        print("C")

    def showC(self):
        self.__showC()

    # protected
    def _showD(self):
        print("D")

    # .ctor
    def __init__(self) -> None:
        print(".ctor 1")

    # multi ctor not support?
    # def __init__(self,str1) -> None:
    #     print(".ctor 2"+str1)

class A(BaseClass):
    def showA(self):
        print("A:AAAA")
    def showAA(self):
        print("A:showAA")
    # __bases__ not in instance
    def getBases(self)->tuple:
        return self.__bases__

class B(BaseClass):
    def showA(self):
        print("B:AAAA")
    def showB(self,ha):
        print("B:BBBB"+ha)
    def showD(self):
        self._showD()

class AB(A,B):
    pass

base = BaseClass()
a = A()
b = B()


print("======base======")
base.showA()
base.showB()
base.showC()
print("======a======")
a.showA()
a.showB()
print("has showAA:%r"%hasattr(a,"showAA"))
print("has showBB:%r"%hasattr(a,"showBB"))
print("a.__bases:%s"%A.__bases__)
print("A.__name__:%s"%A.__name__)
print("======b======")
b.showA()
b.showB("bbbb")
b.showD()


print("======ab======")
ab = AB()
BaseClass.showA(ab)
A.showA(ab)
B.showA(ab)
print("A is subclass of BaseClass:%r"%issubclass(A,BaseClass))
print("AB is subclass of BaseClass:%r"%issubclass(AB,BaseClass))
print("AB is subclass of object:%r"%issubclass(AB,object))
print("B is subclass of AB:%r"%issubclass(B,AB))
print("ab is instance of AB:%r"%isinstance(ab,AB))
print("ab is instance of BaseClass:%r"%isinstance(ab,BaseClass))
print("ab is type of BaseClass:%r"% (type(ab)==BaseClass))
print("ab is type of AB:%r"% (type(ab)==AB))
