def show_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit(balance):
    amount = float(input("Enter amount to deposit: "))
    return balance + amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficent funds!")
        return balance
    return balance - amount

def logout(name):
    print(f"Goodbye {name}! ")

