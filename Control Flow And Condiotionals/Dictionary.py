#  Here we have key value pair
# For example
my_d = {1:"Home", 2:"About"}
my_d[1] = 'Giza'
my_d [3] = 'None'
print(my_d)


# args
# for example
def sum_of(a, b):
 return a+b
print(sum_of(5,4))

# for  parameters in the sum when more than two then it will throw an error that only two are expected so that where args come into

def sum_args(*args):
    total = 0
    for x in args:
        total += x
    return total

print(sum_args(2, 3, 5, 6, 7, 7, 4))
