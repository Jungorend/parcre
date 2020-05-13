from bank import Bank
from person import Person

if __name__ == "__main__":
    bank = Bank(1)
    tom = Person()
    tom.bankAccount = bank.createAccount()
    print(f"Bank Account {tom.bankAccount}")
