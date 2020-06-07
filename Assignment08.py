# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# HChung, 6.6.2020,Modified code to complete assignment 8
# HChung, 6.6.2020,Added error-handling
# HChung, 6.6.2020,Cleaned-up Script (e.g. removed TODOs)
# HChung, 6.7.2020,Updated error-handling so Command Window doesn't immediately close when exception is raised
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []


class Product: # This is our custom class
    """Stores data about a product:
    properties:
        product_name: (string) with the product's  name
        product_price: (float) with the product's standard price
    methods:
        __str__(): converts entire set of attributes to a string
    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        HChung, 6.6.2020,Modified code to complete Assignment 8
    """

    # --Constructor-- # Used to set initial values and automatically runs when you create an object from the class
    def __init__(self, product_name, product_price):
        # --Attributes--
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)  # converts product price from string to float
        except Exception as e:
            raise Exception("Error setting initial values: \n" + str(e))
    # --Properties--
    # Product Name
    @property # Getter properties let you add code to format a field's or attribute's data
    def product_name(self):  # (getter or accessor)
        return str(self.__product_name).title()  # Title case, __ makes attribute "private"

    @product_name.setter # Setter properties let you add code for both validation and error handling
    def product_name(self, value: str):  # (setter or mutator)
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    # Product Price
    @property
    def product_price(self):  # (getter or accessor)
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value: float):  # (setter or mutator)
        if str(value).isnumeric():
            self.__product_price = float(value)
        else:
            raise Exception("Prices must be numbers")

    # --Methods--
    def __str__(self): # to string method
        """ Converts product data to string """
        return self.product_name + "," + str(self.product_price)

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #


class FileProcessor:

    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (Who,When,What)
        RRoot,1.1.2030,Created Class
        HChung, 6.6.2020,Modified code to complete Assignment 8
    """

    @staticmethod
    def save_data_to_file(file_name, list_of_product_objects):
        """ Saves data to a file
        :param file_name: (string) with name of file
        :param list_of_product_objects: (list) of data rows saved to file
        :return: nothing
        """
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(str(row)+"\n") # calls __str__()
        file.close()
        print("Data Saved!")

    @staticmethod
    def read_data_from_file(file_name):
        """ Read rows of data from a file into a list
        :param file_name: (string) with name of file
        :return: (list) of data rows read from the file
        """
        list_of_product_objects = [] # initialize the list of variable before using it

        for row in open(file_name, "r"):
            list_of_product_objects.append(row.strip())  # read one row of data in the file per loop
        return list_of_product_objects


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #


class IO:
    """ Performs Input and Output Tasks

    methods:
        print_menu_items(): -> string menu
        print_current_list_items(list_of_rows): -> list of objects
        input_product_data(): -> object
    changelog: (Who,When,What)
        HChung, 6.6.2020,Created class to complete Assignment 8
    """
    # Note: Below code was adapted from Assignment 06

    @staticmethod
    def print_menu_items():
        """Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Show Current Data
        2) Add a New Item
        3) Save Data to File
        4) Exit the Program
        ''')
        print() # Add an extra line for looks

    @ staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return:string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print() # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_items(list_of_rows:list):
        """ Shows the current items in list of rows
        :param list of rows: (list) of rows you want to display
        :return: nothing
        """
        print("--- Current Product List ---")
        for row in list_of_rows:
            print(row, sep="\n")

    @staticmethod
    def input_product_data():
        """ Gets product data from user

        :return: list
        """
        while True:
            try:
                name = str(input("What is the product name? ")).strip()
                if name.isalpha() == False:
                    raise Exception("That was not a name. Try again.")
                price = str(input("What is the item price? ")).strip()
                if price.isnumeric() == False:
                    raise Exception("That was not a number. Try again.")
                objectP = Product(name, price)
                print(objectP.__str__())
                print() # Add an extra line for looks
                return objectP

            except Exception as e:
                print(e)
                print() # Add an extra line for looks

# # Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of product objects when script starts

try:
    lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)

    while True:
        # Show user a menu of options
        IO.print_menu_items()
        # Get user's menu option choice
        strChoice = IO.input_menu_choice()
        if strChoice.strip() == '1':
            # Show user current data in the list of product objects
            IO.print_current_items(lstOfProductObjects)
            continue
        elif strChoice.strip() == '2':
            # Let user add data to the list of product objects
            lstOfProductObjects.append(IO.input_product_data())
            continue
        elif strChoice.strip() == '3':
            # Let user save current data to file and exit program
            FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
            continue
        elif strChoice.strip() == '4':  # Exit the Program
            input("Press the Enter Key to exit the Program. Goodbye!")
            break # and Exit
        else:
            print("Please Enter 1, 2, 3, or 4!")

except FileNotFoundError as e:
    print("Text file " + strFileName + " must exist before running this script!")
    print(e, e.__doc__, type(e), sep='\n')
    input("Press Enter to Exit the Program")

except Exception as e:
    print("There was an error! Check file permissions.")
    print(e, e.__doc__, type(e), sep='\n')
    input("Press Enter to Exit the Program")

# Main Body of Script  ---------------------------------------------------- #

# # Test the Code ----------------------------------------------------------- #
# # Testing Product Class Code:
# print(Product.__doc__)
# objP1 = Product("ProdA", 9)
# print(objP1.__str__())
# lstOfProductObjects.append(objP1)
#
# Testing FileProcessor Class Code:
# objP1 = Product("chair", 9.99)
# objP2 = Product("table", 30)
# lstOfProductObjects = [objP1, objP2]
# FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
# try:
#     lstOfProductObjects = FileProcessor.read_data_from_file(strFileName)
#     # print(FileProcessor.read_data_from_file(strFileName))
#
# except FileNotFoundError as e:
#     print("Text file " + strFileName + " must exist before running this script!")
#     print(e, e.__doc__, type(e), sep='\n')
#     input("Press Enter to Exit the Program")

# # Testing Presentation Class Code:
# IO.print_menu_items()
# objP1 = Product("chair", 9.99)
# objP2 = Product("table", 30)
# lstOfProductObjects = [objP1, objP2]
# IO.print_current_items(lstOfProductObjects)
# IO.input_product_data()
