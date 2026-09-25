
def load_inventory():
    try:
        file = open("orders.txt","r+")
    except:
        file = open("orders.txt","w+")

    print("Current Orders:")
    if file.read() == "":
        print("No order currently.")
    else:
      print(file.read())
    return file

def get_valid_input(order_list):
    product_name = input("Enter Product Name: ")
    stock = input("Enter Quantity: ")
    if stock.lower() == "quit":
        return stock.lower()
    elif stock.isdigit():
        order_list.append(f"{product_name}, {stock}")
    else:
        raise Exception("Stock amount must be a positive number")

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1

def generate_report(total_units, failed_attempts):
    return f'Total: {total_units}, Failed Attempts: {failed_attempts}'

def save_inventory():
    return

# constant loop
while True:
    load_inventory()



