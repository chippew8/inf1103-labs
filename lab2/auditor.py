inventory = 0
fail_count = 0

# constant loop
while True:
    try:
        # check inventory > 500
        if inventory > 500:
            print("ALERT: INVENTORY IS OVER 500")
            break

        user_input = input("Enter stock amount: ")

        if user_input.lower() == "quit":
            print(f"Total units processed: {inventory}")
            print(f"Number of fails: {fail_count}")
            break

        # check if it's a number 
        elif user_input.isdigit():
            # check if it's positive
            if int(user_input) >= 0:
                inventory += int(user_input)
            else:
                fail_count += 1
                raise Exception("Stock amount must be positive")
        else:
            fail_count +=1
            raise Exception("Stock amount must be a number in digits and positive")
    except Exception as e:
        print(e)


