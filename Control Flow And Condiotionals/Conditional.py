# Here are the conditional statement with if else

# currnet = False
# if currnet:
#     currnet = False
#     print('light switched off')
# if not currnet:
#     currnet= True
#     print("Turning on the light")


# current = True

# if current:
#     current = False
#     print("Hello light os off")
# else:
#     current = True
#     print ("Light is on")

# Elif for loops with many required conditionals

Loyalty_Customer = True
Total_Bills = 99

if Loyalty_Customer and Total_Bills>100 :
    # give 20% discount
   Total_Bills= Total_Bills- (float(Total_Bills)/100)*20
elif Total_Bills>100:
    # give only 10% discount
    Total_Bills=Total_Bills - (float(Total_Bills)/100)*10
else:
    print("Sorry no discount applied")
print("Total bill:", float(Total_Bills))


# Begining of the switch statement
http_request = 500

if http_request == 200 or  http_request==201:
    print("Success")
elif http_request ==400:
    print("Bad request")
elif http_request == 404:
    print("Not Found")
elif http_request == 500 or http_request == 501:
    print("Server error")
else:
    print("Not Found")


    # With switch in python we use match statement for condionals

match http_request:
        case 200 | 201:
            print("success")
        case 400:
            print("Bad request")
        case 404:
            print("Not found")
        case 500 | 501:
            print("Server error")
        case _ :
            print("Not found")

# Loop
# For Loop

for i in range(10):
    print("Count from", i)

favourite = ['chicken', 'Meat', 'potatoes', 'Cabages']
for items in(favourite):
    print("I love", items)


# While loops
count = 0
while count <len(favourite):
    print("I love this dessert", favourite[count]);
    count +=1

    # Controll flow of loops

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert) 
        pass
    else:
        print('No sorry, that dessert is not on my list')


# For nested loops we  have first or the outer loop iterated then the inner one is the after outer loop is completed
# Outer Loops

import time
start_time = time.time()
for i in range(10):
    for j in range(100):
        print(0, end= "")
        print()
    print (round(( time.time() - start_time), 2))