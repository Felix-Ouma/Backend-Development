class A:
    def b(self):
        return "Function insde A"
class B:
    def b(self):
        return "Function inside B"
class C(A,B):
    def d(self):
        return "Function inside C"
    pass
class D(C):
    pass
d = D()
print (d.b())