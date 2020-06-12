# The City is the big ol entity manager. for now the world that exists is just in the scope of
# the city
from functools import reduce
from random import choice,randint

from .bank import Bank
from .person import Person,startingClasses
from .company import Company
from .commodity import commodity_types
from .configuration import Config as CONFIG

class City:
    def __init__(self):
        # Generates the world
        self.banks = []
        self.people = []
        self.companies = []
        self.commodities = []
        self.ticker = 0

        # To Memoize the marketAverages
        # Format is Commodity = [Updated, Price]
        self.averages = {}

        for i in range(0,CONFIG.initialBanks):
            self.banks.append(Bank(i))
            totalPeople = int(CONFIG.initialPeople/CONFIG.initialBanks)
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
            else:
                person.skills = [choice(startingClasses['worker']['skills'])]
        # Initialize the commodity markets so there's stuff to buy initially
        goods = list(commodity_types.keys())
        for i in range(CONFIG.startingCommodities):
            x = choice(goods)
            self.commodities.append(['Init', x, commodity_types[x]['accessibility']])
        for x in commodity_types:
            self.averages[x] = [False, 0]


    def getJobPostings(self):
        "Returns a list of each posting, showing [companyID position wages]"
        postings = []
        i = 0
        for company in self.companies:
            for post in company.jobPostings:
                postings.append([i,post])
            i += 1
        return postings

    def jobApply(self, person, offer):
        "This is a request from a person to a job offer. It needs to create the link and associate the company"
        person.hired(self.companies[offer[0]], offer[1])
        self.companies[offer[0]].hireEmployee(person, offer[1])


    # Memoizes the averages so that if multiple checks or calls are made it's in o[1] time
    # Only makes the checks if there have been any changes
    def marketAverage(self,commodity):
        if self.averages[commodity][0]:
            return self.averages[commodity][1]
        commodities = filter(lambda x: True if commodity == x[1] else False, self.commodities)
        x,y = 0,0
        for i in commodities:
            x += 1
            y += i[2]
        self.averages[commodity] = [True, y/x]
        return self.averages[commodity][1]


    def update(self):
        "Update the world"
        self.ticker += 1
        for i in self.companies:
            i.update(self.ticker)
        for i in self.people:
            i.update(self, self.ticker)


