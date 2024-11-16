# can we assign variable to empty class ?
# it is possible


class Students:
    loaction = "ajmer"

    def __init__(self, name):
        self.name = name


obj = Students("jp")
print(obj)
obj.Name = "sandeep"  # dynamically
print(obj.__dict__)
obj.age = 20

# print(obj.Name)
# print(obj.age)


print(obj.__dict__)


# concept 1

# class = empty (we can assign only varibles )

# concept 2

# at run time dictionary will be created
