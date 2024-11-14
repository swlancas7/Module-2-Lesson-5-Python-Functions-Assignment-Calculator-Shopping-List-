#1. The Calculator App

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enther the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

if operator == "+":
    result = num1 + num2
    print(round(result), 3)
elif operator == "-":
    result = num1 - num2
    print(round(result, 3))
elif operator == "*":
    result = num1 * num2
    print(round(result, 3))
elif operator == "/":
    result = num1 / num2
    print(round(result, 3))
else:
    print(f'{operator} is not a valid operator')

# 2. The Shopping List Maker

def mainMenu():
    print (Shopping List)
           
selection = input("Make your selection: ")
           
if selection == "1":
    displayList()
elif selection == "2":
    addItem()
elif selection == "3":
    removeItem()
else: 
    print("You did not make a valid selection.")

shopping_list = ["apples", "bananas", "carrots", "dates"]
           
def displayList():
    print()
    print("---SHOPPING LIST---")
    
    for i in shopping_list:
        print("* " + i)   

def addItem():
    item = input("Enter item you wish to add to the shopping 
list.: ")
shopping_list.append(item)
print(item + " has been added to the shopping list.")

def removeItem():
    item = input("Which item would you like to remove from the shopping list: ")      
    shopping_list.remove(item
    print(item + "has been removed from the shopping list.")
mainMenu()]

def print_formatted_list(my_list):
    for item in my_list:
        print(f"- {item}")

my_list = [1, 2, 3, 4, 5]
print_formatted_list(my_list)