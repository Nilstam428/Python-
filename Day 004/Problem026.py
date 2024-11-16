# Q26. what is Encapsulation?


# concept 1  public , private, protected

# encapsulation = hideing some information and showing only important information

# private = __(double underscrow)
# protected = _(single underscrow)


class A:

    def __init__(self, name):
        self.__name = name
        print(f"name :{self.__name}")

    def info(self):
        print("this is public functon")


obj = A("jp")
obj.info()
