class A:
    def show(self):
        print("A show function")
class B(A):
    def show(self):
        A.show(self)
        print("B show function")
class C(B):
    def show(self):
        B.show(self)
        print("C show function")
c1=C()
c1.show()
