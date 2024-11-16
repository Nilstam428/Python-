# Q14. explain multilevel inheritance ?


# class Parent:
#     # lang = "python"

#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
#         print("calling from constructor")

#     def info(self):
#         print(f"name : {self.name}")


# class child(Parent):

#     def add(self, a, b):
#         return a + b

#     def info(self):
#         print(f"nameasdlkfjaodkja")
#         super().info()


# obj = child("jp", 21, "jaipur")
# obj.info()


# class A:
#     def add(self, a, b):
#         return a + b


# class B(A):
#     def sub(self, a, b):
#         return a - b


# class C(B):
#     def mul(self, a, b):
#         return a * b


# obj = C()
# print(obj.add(2, 3))
# print(obj.sub(2, 3))
# print(obj.mul(2, 3))


class A:
    def add(self, a, b):
        return a + b


class B(A):
    def mul(self, a, b):
        print(a - b)


class C(B):
    def mul(self, a, b):
        super().mul(a, b)
        return a * b


obj = C()
print(obj.add(2, 3))
# print(obj.sub(2, 3))
print(obj.mul(2, 3))


# fast move = Ctrl + left or right arrow


# def add(a, b):
#     print("this will not print")
#     return a + b
#     print("this will not print")


# add(2, 3)
