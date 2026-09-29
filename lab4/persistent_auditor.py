
def load_inventory():
    # open file
    try:
        with open("./orders.txt","r") as file:
            print("\nCurrent Orders: ")
            file_result = file.read()
            if file_result == "": 
                print("No orders currently\n")
            else: 
                print(file_result)
    except:
        with open("./orders.txt","w+") as file:
            print("\nCurrent Orders")
            if file.read() == "": 
                print("No orders currently\n")
            else: 
                print(file.read())
    return
def get_valid_input(history):
    with open("orders.txt", "r") as file:
        id = 1001
        order_list = file.readlines()
        if order_list != []:
            last = order_list[-1].split(", ")[0]
            id = int(last)+1
        
    product_name = input("Enter Product Name: ")
    if product_name == "quit":
        return product_name
    stock = input("Enter Quantity: ")
    if stock.isdigit():
        finalized = f"{id}, {product_name}, {stock}\n"
        history.append(finalized)
        print("\nNew Order Added:")
        print(finalized)
        return history
    else:
        raise Exception("Stock amount must be a positive number")

def save_inventory(history):
    file = open("./orders.txt", mode="a")
    file.writelines(history)
    file.close()
    print("Order successfully saved to orders.txt")
    

history = []
load_inventory()
while True:
    loop_answer = get_valid_input(history)
    if loop_answer == "quit":
        save_inventory(history)
        break
    
