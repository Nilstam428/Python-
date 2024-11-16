# Q23. what is function overloading and overriding ?


class A:

    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c


obj = A()
print(obj.add(2, 3, 5))
print(obj.add(2, 3, 4))  # error


# concpet 1

# name = "ram"
# print(name)

# name = "radha"

# print(name)


# concept 2
# python does not support method overloading
