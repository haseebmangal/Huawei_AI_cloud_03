
# creating class

# class House:
#     rooms = 4

#     def __init__(self, owner: str, address: str) -> None:
#         self.owner = owner
#         self.address = address

#     def display(self):

#         print(f"Owner: {self.owner}")
#         print(f"Address: {self.address}")

   

# def main():
#     house_1 = House("Alice", "123 Main St")
#     house_1.display()
#     print(f"Rooms: {house_1.rooms}")

# 02 Add a class attribute tax_rate = 0.10 and a method price_with_tax(). create two products,
#  then run product.tax_rate = 0.15. both products should now use the new rate.
# replace the limit parameter of is_low_stock with a class attribute low_stock_limit = 5.

# class Product:

#     tax_rate = 0.10
#     low_stock_limit = 5

#     def __init__(self, name : str, price : float, stock : int) -> None:
#         self.name = name
#         self.price = price
#         self.stock = stock

#     def price_with_tax(self) -> float:
#         return self.price * (1 + Product.tax_rate)

#     def is_low_stock(self) -> bool:
#         return self.stock <= Product.low_stock_limit


# product1 = Product("Laptop", 67000, 7)
# product2 = Product("Mobile", 63000, 12)

# print("___Initial state___")
# print(f"Product 1: {product1.name}, Price with tax: {product1.price_with_tax()}")
# print(f"Product 2: {product2.name}, price with tax: {product2.price_with_tax()}")






# 3 write a shelf class that holds products in a list. it needs add(product) and total_value(). 
# create two shelves and prove that they do not share their products.

# class Shelf:
#     def __init__(self) -> None:
#         self.products = []

#     def add(self, product: Product) -> None:
#         self.products.append(product)


#     def total_value(self) -> float:
#         return sum(product.price_with_tax() for product in self.products)

# shelf1 = Shelf()
# shelf2 = Shelf()


# class Product:
#     def __init__(self, name : str, price : float, stock : int) -> None:
#         self.name = name
#         self.price = price
#         self.stock = stock

# class CartItem:
#     def __init__(self, product: Product, quantity: int) -> None:
#         self.product = product
#         self.quantity = quantity

#     def sub_total(self) -> float:
#         return self.product.price * self.quantity

# class Cart:
#     def __init__(self) -> None:
#         self.items = []

#     def add(self, product: Product, quantity: int) -> None:
#         if quantity > product.stock:
#             print(f"Cannot add {quantity} of {product.name}. Only {product.stock} in stock.")
#             return
#         self.items.append(CartItem(product, quantity))

#     def total(self) -> float:
#         total = 0
#         for item in self.items:
#             total += item.sub_total()
#         return total

#  # add count items method to cart. it returns the total number of units in the cart.(not the number of lines). with 2 notebooks and 3 backpacks in the cart it should return 5.
#     def count_items(self) -> int:
#         return sum(item.quantity for item in self.items)

# def main():
#     notebook = Product("Notebook", 5.0, 10)
#     backpack = Product("Backpack", 50.0, 5)

#     print(f"Notebook name: {notebook.name}, Stock: {notebook.stock}")
#     print(f"Backpack name: {backpack.name}, Stock: {backpack.stock}")

   

#     cart = Cart()
#     cart.add(notebook, 3)
#     cart.add(backpack, 2)
#     cart.add(backpack, 6)  # This should print an error message
#     print(f"Total: {cart.total()}")
#     print(count_items)  



# # ADD count_items() to cart. it returns the total number of units in the cart.(not the number of lines). with 2 notebooks and 3 backpacks in the cart it should return 5.

# ASCII

# examples = ["A", "é", "ش", "中", "🙂"]
# for char in examples:
#     encoded = char.encode("utf-8")
#     print(f"Character: {char}")
#     print(f"Unicode code point: {hex(ord(char))}")
#     print(f"UTF-8 bytes: {encoded}")
#     print(f"UTF-8 bytes in hex: {encoded.hex(' ')}")
#     print(f"Number of UTF-8 bytes: {len(encoded)}")
#     print()


# name = "haseeb"
# print(name)

# x = 10
# x = "haseeb"
# x = 3.14
# x = True
# print(x)

# x = 10
# print(x, type(x))
# x = "Hello"
# print(x, type(x))
# x = 3.14
# print(x, type(x))
# x = True
# print(x, type(x))

# values = [10, "Hello", 3.14, True]
# for value in values:
#     print(value, type(value))

# a = 10
# b = 3

# print("Addition:", a + b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("Floor division:", a // b)
# print("Remainder:", a % b)
# print("Power:", a ** b)

# age = 20
# age = 25
# print(age)
# print(age != 18)
# print(age > 18)
# print(age < 18)
# print(age >= 20)
# print(age <= 25)

# age = 20
# has_id = False

# print(age >= 18 or has_id)
# print(True or False)
# print(not True)

# Collection , List, Tuple, Set, Dictionary

# List: ordered, mutable, allows duplicates
# fruits = ["apple", "banana", "cherry"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(fruits.append("mango"))
# print(fruits)
# print(fruits[-1])

# targets = ["Learn AI", "Build Website", "Play Games"]
# print(targets)
# targets.append("Read Book")  # This will return None
# print(targets)
#   # This will print None

# languages = ["Python", "C++",  "Java", "Javascript", "Go", "Ruby", "Kotlin"]
# print(languages[0])
# print(languages[-1])

# slicing
# numbers = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(numbers[0:3])
# print(numbers[3:7])
# print(numbers[1:10:2])

# append vs insert
# cities = ["New York", "London"]
# cities.append("Tokyo")
# print(cities)
# print(cities.insert(1, "Paris"))  # This will print NoneS
# print(cities)

# membership with "in and "not in"
# guest_list = ["Yousaf", "Fatima", "Hamza"]
# if "dawood" in guest_list:
#     print("dawood is in the guest list.")
# else:
#     print("dawood is not in the guest list.")

# guest_list = ["Yousaf", "Fatima", "Hamza"]
# if "dawood" not in guest_list:
#     print("dawood is not in the guest list.")

# Sort the letters, and print the sorted letters
# letters = ["c", "a", "b", "a", "d", "b"]
# letters.sort()
# print(letters)

# Reverse the letters, and print the reversed letters
# letters.reverse()
# print(letters)

# Print the index of letter "b"
# print(letters.index("b"))

# Print the count of letter "a"
# print(letters.count("a"))

# len(), sum(), min(), max()
# scores = [85, 92, 78, 90, 88]
# print(len(scores))

# Print the "Sum" of all scores.
# print(sum(scores))

# Print the minimum scores from the list
# print(min(scores))

# Print the maximum scores from the list
# print(max(scores))

# Print Average score, (Total/number of subjects)
# print(sum(scores) / len(scores))

# create a list called movies with 5 of your favourite movies.
# movies = ["Inception", "The Matrix", "Interstellar", "The Dark Knight", "Pulp Fiction"]
# print("My favourite movies are:", movies)
# print(f"the first movie is {movies[0]} and the last movie is {movies[-1]}")
# movies.append("the shawshank redemption")
# print(movies)
# print(movies.append("the shawshank redemption"))
# print(movies)

# challenge: remove one movie.
# movies.remove("The Matrix")
# print("After removing 'The Matrix':", movies)

# checking the remaining movies in the list
# print("Remaining movies in the list: ", movies)

#  sort the list alphabetically and print the sorted list.
# movies.sort()
# print("Sorted movies:", movies)

# check the index of a movie using .count()
# print(movies.count("Inception")) 

# Tuples: ordered, immutable, allows duplicates
# cord = (34.0, 71.5)
# print(f"first coordinate address: {id(cord)}")

# cord = (78.0, 36.1)
# print(f"second coordinate address: {id(cord)}")

# print(cord)
# print(cord[0])
# print(cord[1])

# create a tuple called my_location
# my_location = (34.0, 71.5)
# print(f"My location is: {my_location}")
# print(f"Latitude: {my_location[0]}, Longitude: {my_location[1]}")
# print(my_location[0] = 10)
# the error i got
#  File "/Users/haseeb/Documents/Ai_cloud_python/Huawei_AI_cloud_03/src/py_exercise/exercise.py", line 302
#     print(my_location[0] = 10)
#           ^^^^^^^^^^^^^^^^
# SyntaxError: expression cannot contain assignment, perhaps you meant "=="?

#  sets: unordered, mutable, no duplicates
# numbers = {1, 2, 2, 3, 3, 4, 5}
# print(numbers)

#  create a set called class_toppings with at least 6 items.
# class_toppings = {"pepperoni", "mushrooms", "onions", "sausage", "double cheese", "extra cheese", "extra cheese", "mushrooms"}
# print(class_toppings)
# class_toppings.add("pineapple")
# print(class_toppings)

# Dictionaries: unordered, mutable, no duplicates stores key value pairs
# student = {
#     "name": "Alice",
#     "age": 20,
#     "major": "Computer Science"
# }

# print(student)
# print(f"name :", student["name"])

# student["age"] = 21
# print(student)

# student["city"] = "peshawar"
# print(student)

# CREATE a dictionary called "me" with keys
me = {
    "name": "Haseeb",
    "age": 20,
    "city": "Peshawar",
    "hobbies": ["reading", "coding", "gaming"],
    "is_student": True
}

print(me)
me["name"]
print(f"My name is {me['name']}.")

me["age"] = 31
print(f"My age is {me['age']}.")

me["favourite_language"] = "python"
print(f"My favourite programming language is {me['favourite_language']}.")






























if __name__ == "__main__":
    def main():
        ...

    main()