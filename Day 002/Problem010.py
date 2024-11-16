# Q find factorial of a number without recursion ?
# num = int(input("Enter a number: "))
# def fact(num):
#   if num < 0:
#     print("Factorial not defined: ")
#   elif num == 0:
#     print("Factorial:  1")
#   else:
#     fact = 1
#     for i in range(1, num + 1):
#       fact = fact * i
#       print("Factorial: ", fact)




# concept 1
# 0! = 1
# -numbers = not defined
# positive number (5 = 5x4x3x2x1)


def factorial(n):
    fact = 1
    if n < 0:
        print("Not defined !")
    elif n == 0:
        print("Factorial : 1")
    else:
        while n != 1:
            fact *= n
            n -= 1
        print(f"factorial : {fact}")


factorial(int(input("Enter a no. ")))


# dynamic programming
