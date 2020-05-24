# The City is the big ol entity manager. for now the world that exists is just in the scope of
# the city
from bank import Bank
from person import Person
from company import Company

initialBanks = 10
initialPeople = 1000


class City:
    def __init__(self):
        # Generates the world
        self.banks = []
        self.people = []
        self.companies = []
        for i in range(0,initialBanks):
            self.banks.append(Bank(i))
            totalPeople = int(initialPeople/initialBanks)
            for j in range(0,totalPeople):
                self.people.append(Person())
                p = self.people[j+(totalPeople*i)]
                p.bankAccount = self.banks[i].createAccount()
                self.banks[i].addFunds(p.bankAccount[1],p.setInitialFunds())
        for person in self.people:
            if person.soclass == 'investor':
                invest = self.banks[person.bankAccount[0]].displayFunds(person.bankAccount[1]) // 2 # TODO: Better decision making for company values
                self.banks[person.bankAccount[0]].addFunds(p.bankAccount[1],-invest)
                newAccount = self.banks[person.bankAccount[0]].createAccount()
                self.banks[person.bankAccount[0]].addFunds(newAccount[1], invest)
                c = Company([self.banks[newAccount[0]], newAccount[1]])
                person.companies.append(c)
                self.companies.append(c)

    def getJobPostings(self):
        "Returns a list of each posting, showing [companyID position wages]"
        postings = []
        i = 0
        for company in self.companies:
            for post in company.jobPostings:
                postings.append([i,post])
            i += 1
        return postings


