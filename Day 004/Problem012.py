# Q12. how to overrides method ?


class A:
    def method(self):
        print("class A")


class B(A):
    def method(self):
        print("class B")
        super().method()


obj = B()

obj.method()
