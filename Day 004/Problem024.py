# Q24. can a function inside a class have unlimited paremeter ?


class A:

    def add(self, *arg):
        sum = 0
        for i in arg:
            sum += i
        print(sum)


obj = A()
obj.add(2, 3)
obj.add(2, 3, 10)
obj.add(2, 3, 10, 20)
