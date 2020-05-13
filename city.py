# The City is the big ol entity manager. for now the world that exists is just in the scope of
# the city
from bank import Bank
from person import Person

initialBanks = 10
initialPeople = 1000


class City:
    def __init__(self):
        # Initialize everything
        self.banks = []
        self.people = []
        for i in range(0,initialBanks):
            self.banks.append(Bank(i))
            totalPeople = int(initialPeople/initialBanks)
            for j in range(0,totalPeople):
                self.people.append(Person())
                p = self.people[j+(totalPeople*i)]
                p.bankAccount = self.banks[i].createAccount()
                self.banks[i].addFunds(p.bankAccount[1],p.setInitialFunds())

