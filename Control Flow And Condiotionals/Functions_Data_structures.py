# functions are used to run a piece of code multiple times to perfom similar task
def multiply(Total_bill, Tax):
    return (Total_bill* Tax)/100.00
print("total tax", multiply(200.00, 25))


# Types of scopes in python
# LEGB
# Local
# Enclosed
# Global
# Block

Globa_scop = 10

def accessglobal():
    enclosed_scope = 5

    def access_enclosed():
        localscope = 20
        print("Here are now the local variables:", localscope)
    
    access_enclosed()  # Call the nested function
    print("Enclosed variable is at this point:", enclosed_scope)

print("Global is here:", Globa_scop)
accessglobal()




# list
# list works as an array in js, the bellow code shows example of list and how it can be manipulated
months = ['January','February', 'march', 'april','may']
months.insert(3, 'August')
months.insert(5, 'june')

for x in months:
    print("These are the months of the year", x)

# Insert add one item at a specific index,
#  Apend add one element at the end
#  extend add many items at the end of a list at ot once




# Tuples

my_tuple = (1, 'string', 4.5, True)
print(my_tuple.index(4.5))



# Sets
