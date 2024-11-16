# Q29. what is abstraction ?

# abstraction = hide some data and show important information only


# class A:

#     def info(self):
#         pass


# obj = A()

# concept 1
# abstract class does not have object
# abstract class jis class ke ender inherit hogi uske ender us function ko define kerna hoga


from abc import ABC, abstractclassmethod


class A(ABC):
    @abstractclassmethod
    def info(self):
        pass

    def jp(self):
        pass


class B(A):
    def info(self):
        print("calling from class B")


obj = B()
obj.jp()


# concept 1
# 1. inbulit module
# import random
# import math

# 2. user defined module
