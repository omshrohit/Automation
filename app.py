print("hello git")
try:
    a=10
    b=int(input("enter a number"))
    c=a/b
except ZeroDivisionError as e:
    print("zero division error")
else:
    print(c)
