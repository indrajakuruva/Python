class ProductApp: 
    def __init__(self):
        self.products = [] # List to store products

    def add_product(self):
        pid = input("Enter Product ID: ")
        name = input("Enter Product Name: ")
        price = float(input("Enter Product Price: "))
        category = input("Enter Product Category: ")
        product = {'pid': pid, 'name': name, 'price': price, 'category': category}
        self.products.append(product)
        print(f"Product '{name}' added successfully!\n")

    def update_product(self):
        pid = input("Enter Product ID to update: ")
        for product in self.products:
            if product['pid'] == pid:
                product['name'] = input("Enter new Product Name: ")
                product['price'] = float(input("Enter new Product Price: "))
                product['category'] = input("Enter new Product Category: ")
                print(f"Product with ID '{pid}' updated successfully!\n")
                return
        print(f"No product found with ID '{pid}'.\n")

    def delete_product(self):
        pid = input("Enter Product ID to delete: ")
        for product in self.products:
            if product['pid'] == pid:
                self.products.remove(product)
                print(f"Product with ID '{pid}' deleted successfully!\n")
                return
        print(f"No product found with ID '{pid}'.\n")

    def get_product_by_pid(self):
        pid = input("Enter Product ID to search: ")
        for product in self.products:
            if product['pid'] == pid:
                print(f"Product found: {product}\n")
                return
        print(f"No product found with ID '{pid}'.\n")

    def get_all_products(self):
        if not self.products:
            print("No products available.\n")
        else:
            for product in self.products:
                print(product)
            print()

    def get_products_by_category(self):
        category = input("Enter category to search: ")
        found_products = [product for product in self.products if product['category'] == category]
        if found_products:
            for product in found_products:
                print(product)
            print()
        else:
            print(f"No products found in category '{category}'.\n")

    def get_products_between_prices(self):
        min_price = float(input("Enter minimum price: "))
        max_price = float(input("Enter maximum price: "))
        found_products = [product for product in self.products if min_price <= product['price'] <= max_price]
        if found_products:
            for product in found_products:
                print(product)
            print()
        else:
            print(f"No products found between prices {min_price} and {max_price}.\n")

    def exit_app(self):
        print("Exiting the application...")
        exit()

def menu():
    app = ProductApp()
    while True:
        print("Product App Menu:")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Get Product by PID")
        print("5. Get All Products")
        print("6. Get Products by Category")
        print("7. Get Products Between Prices")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            app.add_product()
        elif choice == '2':
            app.update_product()
        elif choice == '3':
            app.delete_product()
        elif choice == '4':
            app.get_product_by_pid()
        elif choice == '5':
            app.get_all_products()
        elif choice == '6':
            app.get_products_by_category()
        elif choice == '7':
            app.get_products_between_prices()
        elif choice == '8':
            app.exit_app()
        else:
            print("Invalid choice! Please try again.\n")
menu()
