# # main.py
# from inventory import Inventory
# from product import Electronics, Grocery, Clothing
# from exceptions import *

# def main():
#     inv = Inventory()

#     while True:
#         print("\n===== Inventory Menu =====")
#         print("1. Add Product")
#         print("2. Sell Product")
#         print("3. Search Product")
#         print("4. View All Products")
#         print("5. Save Inventory")
#         print("6. Load Inventory")
#         print("7. Exit")

#         choice = input("Choose option: ")

#         try:
#             if choice == "1":
#                 p_type = input("Enter type (Electronics/Grocery/Clothing): ").lower()
#                 pid = input("ID: ")
#                 name = input("Name: ")
#                 price = float(input("Price: "))
#                 qty = int(input("Quantity: "))

#                 if p_type == "electronics":
#                     brand = input("Brand: ")
#                     warranty = int(input("Warranty (years): "))
#                     p = Electronics(pid, name, price, qty, warranty, brand)

#                 elif p_type == "grocery":
#                     expiry = input("Expiry Date (YYYY-MM-DD): ")
#                     p = Grocery(pid, name, price, qty, expiry)

#                 elif p_type == "clothing":
#                     size = input("Size: ")
#                     material = input("Material: ")
#                     p = Clothing(pid, name, price, qty, size, material)

#                 else:
#                     print("Invalid type.")
#                     continue

#                 inv.add_product(p)
#                 print("Product added.")

#             elif choice == "2":
#                 pid = input("Enter Product ID: ")
#                 qty = int(input("Enter quantity to sell: "))
#                 inv.sell_product(pid, qty)
#                 print("Product sold.")

#             elif choice == "3":
#                 keyword = input("Enter name/type to search: ")
#                 results = inv.search_by_name(keyword) + inv.search_by_type(keyword)
#                 for p in results:
#                     print(p)

#             elif choice == "4":
#                 for p in inv.list_all_products():
#                     print(p)

#             elif choice == "5":
#                 file = input("Filename to save (e.g., data.json): ")
#                 inv.save_to_file(file)
#                 print("Inventory saved.")

#             elif choice == "6":
#                 file = input("Filename to load: ")
#                 inv.load_from_file(file)
#                 print("Inventory loaded.")

#             elif choice == "7":
#                 print("Exiting...")
#                 break

#             else:
#                 print("Invalid choice!")

#         except Exception as e:
#             print(f"Error: {e}")

# if __name__ == "__main__":
#     main()








from inventory import Inventory
from product import Electronics, Grocery, Clothing
from exceptions import *
from colorama import Fore, init

init(autoreset=True)

def print_header(text):
    print(Fore.YELLOW + "\n==== " + text + " ====")

def get_input(prompt, color=Fore.CYAN):
    return input(color + prompt)

def main():
    inv = Inventory()

    while True:
        print_header("Inventory Menu")
        print(Fore.CYAN + "1. Add Product")
        print(Fore.CYAN + "2. Sell Product")
        print(Fore.CYAN + "3. Search Product")
        print(Fore.CYAN + "4. View All Products")
        print(Fore.CYAN + "5. Save Inventory")
        print(Fore.CYAN + "6. Load Inventory")
        print(Fore.CYAN + "7. Exit")

        choice = get_input("Choose option: ", Fore.MAGENTA)

        try:
            if choice == "1":
                print_header("Add Product")
                p_type = get_input("Enter type (Electronics/Grocery/Clothing): ").lower()

                pid = get_input("ID: ")
                name = get_input("Name: ")
                price = float(get_input("Price: "))
                qty = int(get_input("Quantity: "))

                if p_type == "electronics":
                    brand = get_input("Brand: ")
                    warranty = int(get_input("Warranty (years): "))
                    p = Electronics(pid, name, price, qty, warranty, brand)

                elif p_type == "grocery":
                    expiry = get_input("Expiry Date (YYYY-MM-DD): ")
                    p = Grocery(pid, name, price, qty, expiry)

                elif p_type == "clothing":
                    size = get_input("Size: ")
                    material = get_input("Material: ")
                    p = Clothing(pid, name, price, qty, size, material)

                else:
                    print(Fore.RED + "Invalid type.")
                    continue

                inv.add_product(p)
                print(Fore.GREEN + "Product added successfully.")

            elif choice == "2":
                print_header("Sell Product")
                pid = get_input("Enter Product ID: ")
                qty = int(get_input("Enter quantity to sell: "))
                inv.sell_product(pid, qty)
                print(Fore.GREEN + "Product sold successfully.")

            elif choice == "3":
                print_header("Search Product")
                keyword = get_input("Enter name/type to search: ")
                results = inv.search_by_name(keyword) + inv.search_by_type(keyword)
                if results:
                    for p in results:
                        print(Fore.CYAN + str(p))
                else:
                    print(Fore.RED + "No products found.")

            elif choice == "4":
                print_header("View All Products")
                products = inv.list_all_products()
                if products:
                    for p in products:
                        print(Fore.CYAN + str(p))
                else:
                    print(Fore.RED + "No products in inventory.")

            elif choice == "5":
                print_header("Save Inventory")
                file = get_input("Filename to save (e.g., data.json): ")
                inv.save_to_file(file)
                print(Fore.GREEN + "Inventory saved successfully.")

            elif choice == "6":
                print_header("Load Inventory")
                file = get_input("Filename to load: ")
                inv.load_from_file(file)
                print(Fore.GREEN + "Inventory loaded successfully.")

            elif choice == "7":
                print(Fore.RED + "Exiting...")
                break

            else:
                print(Fore.RED + "Invalid choice! Please try again.")

        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    main()







