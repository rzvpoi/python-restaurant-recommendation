from restaurantData import *

def search_types(input_type):
    recommendationList = []
    for food_type in types:
        if match(input_type, food_type) == True:
            recommendationList.append(food_type)

    return recommendationList

def match(substring, string):
    for idx in range(len(substring)):
        if substring[idx] != string[idx]:
            return False

    return True

def search_restaurant(food_type):
    restaurantList = []
    for restaurant in restaurant_data:
        if food_type == restaurant[0]:
            restaurantList.append(restaurant)

    return restaurantList

def print_restaurants(restaurantList):
    print(f"\nThe restaurants serving {restaurantList[0][0].upper()} food are:\n")
    for restaurant in restaurantList:
        print("--------------------------\n")
        print(f"Name: {restaurant[1]}")
        print(f"Prices: {restaurant[2]}/5")
        print(f"Rating: {restaurant[3]}/5")
        print(f"Address: {restaurant[4]}")
        print("\n")

option = 'y'
print("Welcome to Boyo Restaurant recommendation!")
while option == 'y':
    print("\nWhat type of food would you like to eat?")
    food_type =input("Input the name or some letters to see the results!\n ->")
    result = search_types(food_type)
    if len(result) > 1 :
        print("Found the following food types "+ str(result))
        food_type =input("Input the name to see restaurant results!\n ->")
        result = search_types(food_type)
    elif len(result) == 0:
        option = input("Food type not found!\nWould you like to search for other food type? (y/n): ")
        continue
    
    if len(result) == 1:
        print(f"The only food type for \"{food_type}\" is {result[0]}")
        restaurant_option = input(f"Search for {result[0]} restaurants? (y/n): ")
        if restaurant_option == 'n':
            continue
    else:
        option = input("Food type not found!\nWould you like to search for other food type? (y/n): ")
        continue

    result = search_restaurant(result[0])
    print_restaurants(result)
    option = input("Would you like to continue? (y/n): ")

print("Thank you for visiting Boyo restaurant!")


    


