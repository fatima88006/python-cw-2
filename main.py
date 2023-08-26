my_name= input("What is your name?")
my_age= input("How old are you?")
print(f"My name is {my_name} and I am {my_age} years old")


num1=int(input("Enter first number?"))
num2=int(input("Enter secound number?")) 
operation=(input("Give me operation {+-*/}?"))
if operation == "+":
    print("num1 + num2")
elif operation == "-": 
    print("num1 - num2")
elif operation == "*": 
    print("num1 * num2")
elif operation == "/":
    print("num1 / num2")
else :
    print("the operation is not valid")

bus_capacity=47
people_inbus=int(input("how many people inside the bus?"))
people_out_bus=int(input("how many people are waiting outside?"))
empty_seats = bus_capacity - people_inbus
if empty_seats >= people_out_bus:  
    print(f"there are {empty_seats} seats that can join the bus")
else :
    print("the bus is full")







