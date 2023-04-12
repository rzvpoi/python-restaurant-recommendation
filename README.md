# python-restaurant-recommendation

The python program utilizes a restaurant data module, which contains a list of restaurants with details such as the type of cuisine, name, price range, rating, and address. The first function, search_types, takes an input type and searches through the types of cuisine in the types list. The match function is used to compare the input substring to each string in the types list. If a match is found, the food type is added to a recommendationList. The function then returns the recommendationList containing all matching food types.

The search_restaurant function takes a food type as input and searches through the restaurant_data list for restaurants that serve that cuisine. It then returns a restaurantList containing all matching restaurants.

Finally, the print_restaurants function is used to display the details of the recommended restaurants. It takes the restaurantList as input and prints the name, price range, rating, and address of each restaurant.

The program begins by welcoming the user and prompting them to enter the type of food they would like to eat. If the input matches multiple food types, the program displays all matching food types and prompts the user to enter the specific food type they are interested in. If the input does not match any food types, the user is given the option to search for a different food type.

Once the food type is determined, the program searches for restaurants that serve that cuisine using the search_restaurant function. If the program finds restaurants that serve the food type, it calls the print_restaurants function to display the details of each restaurant.

After displaying the restaurant details, the program prompts the user to continue searching for restaurants or to end the program. If the user chooses to continue searching, the program begins the process again. If the user chooses to end the program, the program prints a final message thanking the user for using the Boyo Restaurant recommendation program.

In conclusion, this Python program provides a user-friendly and efficient way to search for restaurants serving a particular cuisine. The program utilizes simple functions to search through data and display results, making it easy for users to find the perfect restaurant for their next meal.
