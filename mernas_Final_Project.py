"""
Merna Saad
Class: CS 521 - Spring 1
Date: 02/27/2022
Final Project: Shopping List
"""
import datetime
import sys

# Create the main menu
class Shopping_list():
    def __init__(self, elements):
        self.__elements = elements
        # Keep track of the created timestamp as a private attribute
        self.__created_ts = datetime.datetime.now()

    # Displays all items on the shopping list
    def displayList(self):
        print("--- SHOPPING LIST ---")
        for i in self.__elements:
            i = set(i.split(','))
            print(i)

    # Adds an item to the shopping list
    def addItem(self):
        item = input("Enter the item you wish to add to the shopping list: ")
        if item.isdigit():
            print("Oh sorry, please try again, you entered a number.")
        else:
            self.__elements.append(item)
            print(item + " has been added to the shopping list.")
    # Remove an item from the shopping list
    def removeItem(self):
        item = input("Enter the item you wish to remove from the shopping list: ")
        self.__elements.remove(item)
        print(item + " has been removed from the shopping list.")

    # Check to see if a particular item is on the shopping list
    def checkItem(self):
        item = input("What item would you like to check on the shopping list: ")
        if item in self.__elements:
            print("Yes, " + item + " is on the shopping list.")
        else:
            print("No, " + item + " is not on the shopping list.")

    # How many items are on the shopping list
    def listLenght(self):
        assert len(self.__elements) > 0, 'Your list is empty'
        print("There are", len(self.__elements), "items on the shopping list.")

    # Get total of selected item
    def getTotal(self):
        item = input("Please enter the name of the item: ")
        price = float(input("Price: $"))
        quantity = int(input("Quantity: "))
        # Process data
        total_price = price * quantity
        # Output receipt
        print("Your receipt: ")
        print("   Purchased item: " + " " + item.lower())
        print("   Price: $" + str(price))
        print("   Quantity: " + str(quantity))
        print("   Total price: $" + str(total_price))

    # Save your list into text file
    def saveList(self):
        try:
            with open("save_data.txt", "w") as out:
                for element in self.__elements:
                    out.write('%s\n' % element)
                print("Your list is saved successfully")
        except:
            print("Unable to write data!")

    # Remove everything from the shopping list
    def clearList(self):
        self.__elements.clear()
        print("The shopping list is now empty.")

# Unit Tests
if __name__ == "__main__":
    elements = []
    shop = Shopping_list(elements)
    while True:
        print('''### SHOPPING LIST ###
      Select a number for the action that you would like to do:
      1. View shopping list
      2. Add item to shopping list
      3. Remove item from shopping list
      4. Check if item is on shopping list
      5. How many items on shopping list
      6. Clear shopping list
      7. Get total of your item
      8. Save my list
      9. Exit
      ''')
        selection = input("Make your selection: ")  # Ask the user to make a selection
        if selection == "1":
            shop.displayList()
        elif selection == "2":
            shop.addItem()
        elif selection == "3":
            shop.removeItem()
        elif selection == "4":
            shop.checkItem()
        elif selection == "5":
            shop.listLenght()
        elif selection == "6":
            shop.clearList()
        elif selection == "7":
            shop.getTotal()
        elif selection == "8":
            shop.saveList()
        elif selection == "9":
            sys.exit()
        else:
            print("You did not make a valid selection.")