from bank import Bank
from person import Person
from city import City
from company import Company

if __name__ == "__main__":
    c = City()
    company_account = c.banks[0].createAccount()
    c.banks[0].addFunds(company_account[1],10000)
    testCompany = Company([c.banks[company_account[0]], company_account[1]])

