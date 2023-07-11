
PRODUCTS = []

def read_from_database():
    f = open("session7\database.txt", "r")
    for line in f:
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price":result[2], "quantity": result[3]}
        PRODUCTS.append(my_dict)

    f.close()


def write_to_database():
     ...
    
   
def show_menu():
    print("1-Add")
    print("2-Edit")
    print("3-Remove")
    print("4-Search")
    print("5-Show List")
    print("6-buy")
    print("7-Exit")
    

def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = ("enter price: ")
    quantity = ("enter quantity: ")
    new_product = {"code": code, "name": name,"price": price, "quantity": quantity}
    PRODUCTS.append(new_product)

def edit():
    ...

def remove():
   ...

def search():
    user_input = input("enter your keyboard: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
          product(product["code"], "\t\t", product["name"], "\t\t", product["price"])  
          break
    else:
        product("not found")


def show_list():
    print("code\tname\tprice\tquantity")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def buy():
    pass
  

print("Welcome to Lagha Store")
print("loading...")
read_from_database()
print("Data loaded.")

print(PRODUCTS)

while True:
    show_menu()
    choice = int(input("enter your choice: "))


    if choice == 1:
        add()
    elif choice == 2:
        edit()
    elif choice == 3:
        remove()
    elif choice == 4:
        show_list()
    elif choice == 5:
        buy()
    elif choice == 6:
        buy()
    elif choice == 7:
        write_to_database()
        exit(0)
    else:
        print("enter num 1-7 :|")







    # read_from_database()
    # #print(PRODUCTS)

    # for product in PRODUCTS:
    #     print(product)