
# import statement
from tabulate import tabulate


# defining a class
class Shoe:

    # empty lists
    country_list = []
    code_list = []
    product_list = []
    cost_list = []
    quantity_list = []
    value_list = []

    # A function that reads data from a file
    @classmethod
    def read_data(cls):

        try:
            # opening a file
            with open("inventory.txt", "r") as file:
                read_file = file.readlines()

                for i in read_file:
                    separator = i.rstrip().split(",")
                    cls.country_list.extend(separator[:1])
                    cls.code_list.extend(separator[1:2])
                    cls.product_list.extend(separator[2:3])
                    cls.cost_list.extend(separator[3:4])
                    cls.quantity_list.extend(separator[4:5])

        except FileNotFoundError:
            print(FileNotFoundError)

    # A function that determines the product with
    # the highest quantity
    @classmethod
    def highest_quantity(cls):

        cls.country_list = cls.country_list[1:]
        cls.code_list = cls.code_list[1:]
        cls.cost_list = cls.cost_list[1:]
        cls.product_list = cls.product_list[1:]
        cls.quantity_list = list(map(int, cls.quantity_list[1:]))

        # finding the highest and index of the highest quantity product
        hi = max(cls.quantity_list)
        high = cls.quantity_list.index(hi)

        # displaying the product with the highest quantity
        print(f"Product with the highest quantity:\n\tCountry: {cls.country_list[high]} \n\tCode: {cls.code_list[high]}"
              f"\n\tProduct: {cls.product_list[high]} \n\tCost: {cls.cost_list[high]} "
              f"\n\tQuantity: {cls.quantity_list[high]}")

        print("\nThis product is for sale.")

    # A function that determines the product with
    # the lowest quantity
    @classmethod
    def lowest_quantity(cls):

        cls.country_list = cls.country_list[1:]
        cls.code_list = cls.code_list[1:]
        cls.cost_list = cls.cost_list[1:]
        cls.product_list = cls.product_list[1:]
        cls.quantity_list = list(map(int, cls.quantity_list[1:]))

        # finding the highest and index of the highest quantity product
        low = min(cls.quantity_list)
        low_index = cls.quantity_list.index(low)

        # displaying the product with the highest quantity
        print(
            f"Product with the lowest quantity:\n\tCountry: {cls.country_list[low_index]} "
            f"\n\tCode: {cls.code_list[low_index]} \n\tProduct: {cls.product_list[low_index]} "
            f"\n\tCost: {cls.cost_list[low_index]} \n\tQuantity: {cls.quantity_list[low_index]}")

        print("This product needs to be restocked")

    # A function that determines the value of each
    # item
    @classmethod
    def value_per_item(cls):

        cls.quantity_list = list(map(int, cls.quantity_list[1:]))
        cls.cost_list = list(map(int, cls.cost_list[1:]))

        for i, j in zip(cls.cost_list, cls.quantity_list):
            v = i * j

            # storing values of items to a list
            cls.value_list.append(v)

        return cls.value_list

    # A function that searches an item by code
    # based on user input
    @staticmethod
    def search(code):

        # opening a file
        with open("inventory.txt", "r") as file_1:
            item = [i.rstrip() for i in file_1 if code in i]
            print(item[0])


# getting user input
choice = input('''Welcome, please input your choice below:
    s - search for a product by code
    lq - determine product with lowest quantity
    hq - determine product with highest quantity
    rd - represent data in a table format
    q - quit
    : ''').lower()

# creating an instance of a Shoe class
obj = Shoe()
obj.read_data()

# evaluating options based on user input
if choice == "s":

    # an object list
    my_objects = []

    for count in range(0, 5):
        try:
            # creating a series of objects
            obj_1 = Shoe()
            obj_2 = Shoe()
            obj_3 = Shoe()
            obj_4 = Shoe()
            obj_5 = Shoe()

            # storing objects to a list
            my_objects.append(obj_1)
            my_objects.append(obj_2)
            my_objects.append(obj_3)
            my_objects.append(obj_4)
            my_objects.append(obj_5)

            # searching products in the objects list by product code
            for ob in my_objects:
                # getting user input
                p_code = input("Enter a product unique code: ")
                ob.search(p_code)
                print()
            break

        except IndexError:
            print("The product code you provided doesn't exists. Try again.")

elif choice == "lq":
    obj.lowest_quantity()

elif choice == "hq":
    obj.highest_quantity()

elif choice == "rd":

    value = obj.value_per_item()
    value[:0] = ["Value"]
    obj.cost_list[:0] = ["Cost"]
    obj.quantity_list[:0] = ["Quantity"]

    # displaying data in a table format
    print(tabulate([obj.country_list, obj.code_list, obj.product_list, obj.cost_list, obj.quantity_list,
                    value]))

elif choice == "q":
    print("Thanks for your interaction with our program. Visit Again.")
    exit()
