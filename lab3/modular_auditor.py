def get_valid_input():
    user_input = input("Enter Stock Amount: ")
    if user_input.lower() == "quit":
        return user_input.lower()
    elif user_input.isdigit():
        return int(user_input)
    else:
        raise Exception("Stock amount must be a positive number")

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.1

def generate_report(total_units, failed_attempts):
    return f'Total: {total_units}, Failed Attempts: {failed_attempts}'

inventory = 0
fail_count = 0
# constant loop
while True:
    try:
        # check inventory > 500
        if inventory > 500:
            print("ALERT: INVENTORY IS OVER 500")
            break

        user_input = get_valid_input()
        if user_input == "quit":
            print(generate_report(inventory, fail_count))
            break
            
        else:
            # check if it's positive
            if user_input >= 0:
                inventory += int(user_input)
            else:
                fail_count += 1
                raise Exception("Stock amount must be positive")
            
    except Exception as e:
        fail_count += 1
        print(e)


