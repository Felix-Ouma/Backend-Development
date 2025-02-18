def divide_by(a,b):
    return a/b


try:
    ans = (divide_by(40,0)) 
except ZeroDivisionError as e:
    print(e, "Something went wrong", e)
    print (e.__class__)
