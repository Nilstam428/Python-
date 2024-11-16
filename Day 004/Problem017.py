# Q17. what is "method resoultion order(MRO)" ?


# concept 1 (bases)


# class A:
#     pass


# class B:
#     pass


# class C(A, B):
#     pass


# obj = B()
# print(C.__bases__)

# concept 2


# class A:
#     pass


# print(A.__bases__)


# every class is inherited from object class


# concept 3

# hybrid = multiple + herichal

# multiple
# class A:
#     pass

# class B:
#     pass

# class C(A,B):
#     pass


# herichal

# class A:
#     pass

# class B(A):
#     pass

# class C(A):
#     pass

# hybrid = combination of multiple and herichal


class A:
    def __init__(self):
        print("class A")
        super().__init__()


class B(A):
    def __init__(self):
        print("class B")
        super().__init__()


class C(A):
    def __init__(self):
        print("class C")
        super().__init__()


class D(B, C):

    def __init__(self):
        print("class D")
        super().__init__()


obj = D()

# print(D.mro())
