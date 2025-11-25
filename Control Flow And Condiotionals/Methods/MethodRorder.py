class A:
    def a(self):
        return 'Function inside A'
class B:
    def a(self):
        return "Function inside B"
class C(B,A):
    pass
c = C()
print (c.a())