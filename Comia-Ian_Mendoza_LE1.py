game_library = {
    "Donkey Kong" : {"quantity": 3, "cost": 2},
    "Super Mario Bros" : {"quantity": 5, "cost":3},
    "Tetris" : {"quantity" : 2, "cost" : 1}
}
user_account = {}

admin_password = "admin"
admin_username = "admin"

def sign_up():
    print("\n---Sign Up---")
    while True:
        try:
            username = input("Enter your usename: ")
            if username in user_account:
                print("Username taken. Try again.")
                sign_up()
            if not username:
                main()
            if username not in user_account:
                points = 0
                balance = 0
                password = input("Enter your password: ")

                if len(password) < 8:
                    print("Password must be at least 8 Characters. Try Again")
                    continue
                else:
                    user_account[username] = {"password" : password, "points" : points, "balance" : balance}
                    print("Sign Up Successful")
                    main()
            else:
                print("Invalid Input")
                sign_up()
        except ValueError as e:
            main()

def sign_in():
    print("\n---Sign In---")
    while True:
        try:
            username = input("Enter your Username: ")
            password = input("Enter your password: ")

            if not username:
                main()
            if username in user_account:
                if user_account[username] and user_account[username]['password'] == password:
                    print("Log In Successful")
                    usermenu(username)
                else:
                    print("Invalid Pasword")
            else:
                print("Invalid Username")
        except ValueError as e:
            main()

def usermenu(username):
    print(f"Welcome to Game Rental {username}")
    while True:
        try:
            print("1. Rent Game")
            print("2. Return Game")
            print("3. Top Up")
            print("4, Display Inventory")
            print("5. Redeem Free Game Rental")
            print("6. Check Points")
            print("7. Log Out")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                rent_game(username)
            if choice == 2:
                return_game(username)
            if choice == 3:
                top_up(username)
            if choice == 4:
                display_available_games()
            if choice == 5:
                redeem_free_game(username)
            if choice == 6:
                checkpoints(username)
            if choice == 7:
                main()
            else: 
                print("Invalid Input")

        except ValueError as e:
            usermenu(username)

def rent_game(username):
    print("---Rent a Game---")
    while True:
        try:
            game_choice = input("Enter your game choice: ")

            if game_choice not in game_library:
                usermenu(username)
            if game_choice in game_library:
                game_quantity = int(input("Enter the quantity of games you want to rent: "))
                if game_quantity > game_library[game_choice]['quantity']:
                    print("Not enough game quantity. Try Again")
                    rent_game(username)
                else:
                    
                    if user_account[username]['balance'] < game_library[game_choice]['cost']:
                        print("Not Enough Balance Top Up first. ")
                        usermenu(username)
                    else:
                        game_library[game_choice]['quantity'] -= game_quantity
                        user_account[username]['balance'] -= game_library[game_choice]['cost']

                        user_account[username]['points'] += (game_library[game_choice]['cost'] // 2) 

                        print("Game Successfully Rented. Thank You")

                        print(f"New User Balance: {user_account[username]['balance']}\n\nNew User Points: {user_account[username]['points']}")

                        usermenu(username)
        except ValueError as e:
            usermenu(username)

def return_game(username):
    print("---Return A Game---")
    while True:
        try:
            game_name = input("Name of the game you want to return: ")
            if not game_name:
                usermenu(username)
            if game_name in game_library:
                game_quantity = int(input("Enter the quantity of games you want to return: "))

                game_library[game_name]['quantity'] += game_quantity

                print("You successfully returned the game")

                usermenu(username)
            else:
                print("Invalid Input")
                return_game(username)
        except ValueError as e:
            usermenu(username)
def top_up(username):
    print("---Top Up---")
    while True:
        try:
            print(f"Current User Balance: {user_account[username]['balance']}.")

            topup = int(input("Enter the amount to top up: "))

            if topup <= 0:
                print("Invalid amount. Try again")
                top_up(username)
            else:
                user_account[username]['balance'] += topup 

                print(f"Top Up successful. \n\n New User Balance: {user_account[username]['balance']}.\n\nReturning to User Menu...")
                usermenu(username)
        except ValueError as e:
            usermenu(username)
    
def checkpoints(username):
    print("---Check User Points---")
    while True:
        print(f"\n\nUser Points: {user_account[username]['points']}")
        print("Returning to User Menu...")
        usermenu(username)

def redeem_free_game(username):
    print("---Redeem Free Game---")
    while True:
        try:
            print(f"\n\nUser Points: {user_account[username]['points']}")

            game_choice = input("Enter the name of the game you want to rent: ")
            if not game_choice:
                usermenu(username)
            if game_choice not in game_library:
                print("Game does not Exist. Try Again")
                redeem_free_game(username)
            if game_choice in game_library:
                if user_account[username]['points'] < game_library[game_choice]['cost']:
                    print("Insufficient Points. Try Again")
                    redeem_free_game(username)
                else: 
                    user_account[username]['points'] -= game_library[game_choice]['cost']
                    game_library[game_choice]['quantity'] -= 1

                    print(f"Successfully Rented {game_choice}")
                    print("Returning to User Menu...")
                    usermenu(username)

        except ValueError as e:
            usermenu(username)

def display_available_games():
    while True:
        for key, value in game_library.items():
            print(f"{key}, Quantity: {game_library[key]['quantity']}")
            main()

def admin():
    print("---Admin Sign In---")
    while True:
        try:
            username = input("Enter your admin username:")
            password = input("Enter your admin password: ")

            if username == admin_username:
                if password == admin_password:
                    adminmenu()
                else:
                    print("Invalid Password")
            else:
                print("Invalid Username")

        except ValueError as e:
            main()

def adminmenu():
    print("---Welcome Admin---")
    while True:
        try:
            print("What would you like to do?\n")
            print("1. Add Game")
            print("2. Change Game Price")
            print("3. Delete/Remove Game")
            choice = int(input("\nEnter your choice: "))

            if not choice:
                main()
            if choice == 1:
                add_game()
            if choice == 2:
                change_price()
            if choice == 3:
                delete_game()
            else:
                print("Invalid Input")

        except ValueError as e:
            adminmenu()
def add_game():
    print("---ADD GAME---")
    while True:
        try:
            new_game_name = input("Enter the name of the new game:" )

            if new_game_name in game_library:
                print("Game Already Exists. Try again")
                add_game()
            if not new_game_name:
                adminmenu()
            if new_game_name not in game_library:
                new_game_quantity = int(input("Enter the quantity of the new game: "))
                if new_game_quantity <= 0:
                    print("Quantity cant be 0 or negative")
                else:
                    new_game_cost = int(input("Enter the price of the new game: "))
                    if new_game_cost == 0:
                        confirmation = str(input("Are sure you want to add a free game? y/n: "))
                        if confirmation == 'y':
                            game_library[new_game_name] = {"quantity" : new_game_quantity, "cost" : new_game_cost}
                            print(f"Successfully Added {new_game_name} to the Game Library")
                            print("Returning to Admin Menu...")
                            adminmenu()
                        if confirmation == 'n':
                            print("Try Again")
                            add_game()
                        else:
                            print("Invalid Input")
                            add_game()
                    else:
                        game_library[new_game_name] = {"quantity" : new_game_quantity, "cost" : new_game_cost}
                        print(f"Successfully Added {new_game_name} to the Game Library")
                        print("Returning to Admin Menu...")
                        adminmenu()
        except ValueError as e:
            adminmenu()

def change_price():
    print("---Change Price---")
    while True:
        try:
            gamename = input("Enter the name of the game you want to change the price of: ")
            if not gamename:
                adminmenu()
            if gamename in game_library:
                new_price = int(input(f"Enter the new price of {gamename}: "))
                if new_price <= 0:
                    print("Invalid Amount. Try again")
                    change_price()
                else:
                    game_library[gamename]['cost'] -= new_price
                    print(f"The new price of {gamename} is {new_price}")
                    print("Returning to Admin Menu")
                    adminmenu()
            else:
                print("Invalid Input")
                adminmenu()
        except ValueError as e:
            adminmenu()
def delete_game():
    print("---Delete Game---")
    while True:
        try:
            gamename = input("Enter the name of the game you want to delete: ")
            if gamename not in gamename:
                print("Game does not exist. Try again")
                delete_game()
            if not gamename:
                adminmenu()
            if gamename in game_library:
                confirmation = input("Are you sure you want to delete the game? y/n: ")
                if confirmation == 'y':
                    del game_library[gamename]
                    print("Game Removed Successfully.")
                if confirmation == 'n':
                    print("Going back to Admin Menu. ")
                    adminmenu()
                else:
                    print("Invalid Input Try Again")
                    delete_game()
            else:
                print("Invalid Input. Try Again")
                delete_game()
        except ValueError as e:
            adminmenu()


def main():
    print("\n---Welcome to ________ ---")
    while True:
        try:
            choice = int(input("\n1. Display Available Games\n\n2. Sign In\n\n3. Log In\n\n4. Admin Login\n\nEnter Choice: "))

            if choice == 1:
                display_available_games()
            if choice == 2:
                sign_up()
            if choice == 3:
                sign_in()
            if choice == 4:
                admin()
            else:
                print("Invalid Input")
        except ValueError as e:
            main()

main()