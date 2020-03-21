from abc import ABC,abstractmethod
class A(ABC):
    @abstractmethod
    def show(self):
        pass
    def fun(self):
        print("fun called")
class B(A):
    def show(self):
        print("show called")
b1=B()
b1.show()
b1.fun()
