# Q18. what will happen when two class have same function and they inherits their properties to other class ?


class A:
    def info(self):
        print("class A")


class B:

    def info(self):
        print("class B")


class C(B, A):
    pass


obj = C()
obj.info()
