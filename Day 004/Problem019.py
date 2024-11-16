# Q19.If class B overrides method of class A and class C inherits properties from class B . can we access method of class A from C's object.


class A:

    def info(self):
        print("class A")


class B(A):

    def info(self):
        print("class B")
        super().info()


class C(B):

    def m1(self):
        print("class C")
        super().info()


obj = C()
obj.m1()


# concept 1
# 1. method = ()
# 2. varibale = .
