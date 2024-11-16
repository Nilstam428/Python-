# Q11. what is the use of super keyword.


# class Students:
#     # lang = "python"

#     def __init__(self, name, age, location):
#         self.name = name
#         self.age = age
#         self.location = location
#         print("calling from constructor")

#     def info(self):
#         print(f"name : {self.name}")


# class Person(Students):

#     def __init__(self, lang, name, age, location):

#         super().__init__(name, age, location)
#         self.lang = lang

#     def jp(self):
#         print("calling from person class")


# obj = Person("python", "jp", 21, "Ajmer")
# obj.info()


class Students:
    # lang = "python"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        print("calling from constructor")

    def info(self):
        print(f"name : {self.name}")


class Person(Students):

    def __init__(self, name, lang):

        super().__init__(name, age=None, location=None)
        self.lang = lang

    def jp(self):
        print("calling from person class")


obj = Person("jp", "java")
obj.info()
