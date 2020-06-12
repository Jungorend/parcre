from math import ceil
from .commodity import commodity_types
from .configuration import Config as CONFIG

class Employee:
    def __init__(self, person, role, wages):
        self.person = person
        self.role = role
        self.wages = wages

class JobPosting:
    def __init__(self, position, wages, maxWages):
        self.position = position
        self.wages = wages
        self.maxWages = maxWages

class Company:
    # Companies when formed will first try to determine what to
    # create and then will put out posting for the jobs they need
    def __init__(self, bankAccount, targetProduct=''):
        self.financing = {'bank': bankAccount[0],
                          'bankAccount': bankAccount[1],
                          'budgeted': 0
        }
        self.employees = {'available': [],
                          'assigned': []}
        self.technologies = []
        self.jobPostings = []
        if targetProduct == '':
            self.targetProduct = self.determineBestProduct()
        else:
            self.targetProduct = targetProduct

        self.hireProjectStaff()
        self.ticker = 0  # Used to determine how frequently to change products, etc.

    # Determine best product will look at market factors to determine what
    # the company should produce, and can be used for staffing decisions accordingly
    # This may need to be outside the company class and more based on what other
    # companies are doing as well
    # TODO: Have this actually work
    def determineBestProduct(self):
        return 'food'

    # TODO: sets price based on existing hiring postings
    def setHiringPrice(self, workerPosition):
        if not self.jobPostings:
            return 1
        else:
            averagePrice = 0
            currentPostings = 0
            for posting in self.jobPostings:
                if posting.position == workerPosition:
                    averagePrice += posting.wages
                    currentPostings += 1
            return ceil(averagePrice / currentPostings)

    def areFundsAvailable(self,funds):
        if self.financing['bank'].displayFunds(self.financing['bankAccount']) - self.financing['budgeted'] > funds:
            return True
        return False

    # Only increases if it thinks it can increase everything
    def updatePostings(self):
        if self.areFundsAvailable(len(self.jobPostings)):
            for j in self.jobPostings:
                if j.wages < j.maxWages:
                    j.wages += 1
                    self.financing['budgeted'] += 1

    def hireEmployee(self, person, offer):
        e = Employee(person, offer.position, offer.wages)
        self.employees['available'].append(e)
        self.jobPostings.remove(offer)


    # TODO: Update so that a commodity can require more than one worker of the same type
    def hireProjectStaff(self):
        """This returns how many roles are needed to add one more project of the
        product to the queue. The resulting targets can then be added to jobPostings,
        and if there's still extra funds left it can be repeated."""
        expenses = 0
        required_roles = []
        new_assignments = [self.targetProduct]

        for tools in commodity_types[self.targetProduct]['dependencies']['tools']:
            # TODO: Implement Market for purchases of goods and tools
            pass

        for deps in commodity_types[self.targetProduct]['dependencies']['workers']:
            found = False
            for e in self.employees['available']:
                if e.role == deps:
                    new_assignments.append(e)
                    break
            if not found:
                expenses += self.setHiringPrice(deps)
                # Max Wage is 1 less than the value / workers, and then reduce one to guarantee profit
                required_roles.append(JobPosting(deps,self.setHiringPrice(deps),self.getCommodityWorth(self.targetProduct)/len(commodity_types[self.targetProduct]['dependencies']['workers']) - 1))
        if required_roles == []:
            self.employees['assigned'].append(new_assignments)
            for e in new_assignments:
                self.employees['available'].remove(e)
        else:
            if not self.areFundsAvailable(expenses):
                return
            self.financing['budgeted'] += expenses
            self.jobPostings.extend(required_roles)

    def work(self):
        pass

    def sell(self):
        pass

    # How much value a commodity has sets a good baseline for if it's worth
    # producing or how much to hire pepole for it. This can then be modified by
    # supply and demand
    # TODO: Accommodate tool prices, potentially difference in education of worker requirements
    def getCommodityWorth(self,commodity):
        return commodity_types[commodity]['accessibility'] * len(commodity_types[commodity]['dependencies']['workers'])

    # Company loop
    # Work employees
    # post items that are made to make profits
    # determine how to expand
    # put up postings for new equipments and jobs
    # TODO: Add research and buy hardware, remove no longer profitable positions, employees
    def update(self,ticker):
        self.work()
        self.sell()
        if ticker % CONFIG.JobPostingUpdate == 0:
            self.updatePostings()
        if ticker % CONFIG.HireUpdate == 0:
            self.determineBestProduct()
            self.hireProjectStaff()





