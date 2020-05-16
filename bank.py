class BankAccount:
    def __init__(self, accountNumber):
        self.funds = 0
        self.acountNumber = accountNumber

class Bank:
    def __init__(self, bankID):
        self.id = bankID
        self.currentID = 0 # This is the current available account ID
        self.accounts = {}

    def createAccount(self):
        self.accounts[self.currentID] = BankAccount(self.currentID)
        self.currentID += 1
        return [self.id, self.currentID - 1] # Currently saves as [bank, account]

    def displayFunds(self, account):
        return self.accounts[account].funds

    def addFunds(self, account, funds):
        self.accounts[account].funds += funds
