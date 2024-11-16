# Q13. explain single level inheritance ?


class Parent:
    # lang = "python"

    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        print("calling from constructor")

    def info(self):
        print(f"name : {self.name}")


class child(Parent):

    def add(self, a, b):
        return a + b

    def info(self):
        print(f"nameasdlkfjaodkja")
        super().info()


obj = child("jp", 21, "jaipur")
obj.info()
