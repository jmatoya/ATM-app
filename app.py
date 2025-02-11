from banking_pkg import account 

def atm_menu(name): 
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("    === Automated Teller Machine ===    ")
while True:
    name = input("Enter name to register: ")
    if 1 <= len(name) <= 20:
        break    
    else:
        print("Error: Name must be between 1 and 10 characters. Try again.")
        continue
while True:
    pin = input("Enter PIN: ")
    if len(pin) == 4 and pin.isdigit():
        break
    else:
        print("Error: Please enter 4 digits.")
        continue
balance = 0
print(f"{name} has been registered with a starting balance of ${str(balance)}")
print("")
while True:
    print("          === Automated Teller Machine ===          ")
    print("LOGIN")
    name_Input = input("Enter name: ")
    pin_Input = input("Enter PIN: ")
    if name_Input == name and pin_Input == pin:
        print("Login in Successful!")
        break
    else:
        print("Invalid credentials!")
    
while True:
    atm_menu(name)
    option = int(input("Choose an option: "))

    if option == 1:
        account.show_balance(balance)
    elif option == 2:
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option ==3:
        balance = account.withdraw(balance)
        account.show_balance(balance)
    elif option == 4:
        account.logout(name)
        break   

