class Product:
    def __init__(self, i, n, p, c):
        self.id = i
        self.name = n
        self.price = p
        self.count = c

    @staticmethod
    def add():
        code = input("enter code: ")
        name = input("enter name: ")
        price = ("enter price: ")
        quantity = ("enter quantity: ")
        #new_product = {"code": code, "name": name,"price": price, "quantity": quantity}
        new_product = Product(code, name, price, quantity)
        PRODUCTS.append(new_product)

    def edit(self):
        ...

    
    def remove(self):
        ...

    @staticmethod
    def search():
        ...
            
    @staticmethod
    def show_list():
        ...

    
    def show(self):
        ...

    
    def buy(self):
        ...


class Database:
    def __init__(self):
        ...
    def read(self):
        f = open("session12\database.txt", "r")
        for line in f:
            result = line.split(",")
        # my_dict = {"code": result[0], "name": result[1], "price":result[2], "quantity": result[3]}
            my_obj = Product(result[0], result[1], result[2], result[3])
            PRODUCTS.append(my_obj)

        f.close()

    def write(self):
        ...

db = Database()
PRODUCTS = []

def show_menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Show List")
    print("6-buy")
    print("7-Exit")

print("Welcome to Lagha Store")
print("loading...")
db.read()
print("Data loaded.")

print(PRODUCTS)

while True:
    show_menu()
    choice = int(input("enter your choice: "))


    if choice == 1:
        Product.add()

    elif choice == 2:
        id = int(input('Enter product id:'))
        for p in PRODUCTS:
            if p.id == id:
                p.edit()
        
    elif choice == 3:
        id = int(input('Enter product id:'))
        for p in PRODUCTS:
            if p.id == id:
                p.remove()

    elif choice == 4:
        Product.search()
        
    elif choice == 5:
        Product.show_list()

    
    elif choice == 6:
        buy()

    elif choice == 7:
        db.write()
        exit(0)
    else:
        print("enter num 1-7 :|")







    # read_from_database()
    # #print(PRODUCTS)

    # for product in PRODUCTS:
    #     print(product)
