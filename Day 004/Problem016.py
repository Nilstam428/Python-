# Q16. access constructor of parent class in child class (multiple inheritance)?


# class A:

#     def __init__(self):
#         print("class A")


# class B:

#     def __init__(self):
#         print("class B")


# class C(A, B):
#     pass


# obj = C()


# class A:

#     def __init__(self):
#         print("class A")


# class B:

#     def __init__(self):
#         print("class B")


# class C(A, B):

#     def __init__(self):
#         print("class c")


# obj = C()


# class A:

#     def __init__(self):
#         print("class A")
#         super().__init__()


# class B:

#     def __init__(self):
#         print("class B")


# class C(A, B):

#     def __init__(self):
#         print("class c")
#         super().__init__()


# obj = C()


# class A:

#     def __init__(self):
#         print("class A")
#         # super().__init__()


# class B:

#     def __init__(self):
#         print("class B")


# class C(A, B):

#     def __init__(self):
#         print("class c")
#         super().__init__()
#         B().__init__()


# obj = C()


# class A:

#     def __init__(self,name):
#         self.name = name
#         print(f"name : {self.name}")
#         # super().__init__()


# class B:

#     def __init__(self,age):
#         self.age= age
#         print(f"age : {self.age}")


# class C(A, B):

#     def __init__(self,location):
#         self.location = location
#         print(f" location : {self.location}")


# obj = C()


class A:

    def __init__(self, name, age):
        self.name = name
        print(f"name : {self.name}")
        super().__init__(age)


class B:

    def __init__(self, age):
        self.age = age
        print(f"age : {self.age}")


class C(A, B):

    def __init__(self, location, name, age):
        self.location = location
        print(f"location : {self.location}")
        super().__init__(name, age)


obj = C("Ajmer", "jp", 21)


# concept 1
# 1. constructor has no return type
# 2. constructor makes instance variable
# 3. class => object => constructor will called


# concept 2
# class A:
#     pass


# obj = A()
# obj.name = "jp"
# obj.age = 21

# print(obj.name)
# print(obj.__dict__)
