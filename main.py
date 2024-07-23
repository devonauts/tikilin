from audioop import add


cars = [
    "Tesla Model S",
    "Ford Mustang",
    "Toyota Corolla",
    "BMW 3 Series",
    "Chevrolet Silverado",
    "Honda Civic",
    "Mercedes-Benz C-Class",
    "Audi A4",
    "Porsche 911",
    "Lexus RX"
]
grocery_list = [

    "apples",
    "bananas",
    "oranges"
]

# def car_adder (thing_to_add, target_list) :
#     if target_list[0].lower() in 'abcdefg':
#         print('this car starts with A-G')
#         target_list.append(thing_to_add)
    
#     else:
#         print("this car starts with H-Z and wr are not allowing it in our club")
#     # for item in target_list:
#     #     if len(item) <= 5:
            
#     #         target_list.remove(item)
#     #         print(f'{item} was not added because it is too few')
    


# car_adder('AASDASDASDASD',groceries)
# print(groceries)


# def addTwo(num):
#     return num + 2

# def addThree(num):
#     return num + 3

# print(addThree(addTwo(2)))

def namePrinter(first, last, middle=''):
    return f'My name is {last}, {first} {middle} {last}.'

# print (namePrinter('James','Bodn'))

def giveMeMyGroceries(thing_to_add):
    grocery_list.append(thing_to_add)
    return grocery_list

print(giveMeMyGroceries('spagethi'))