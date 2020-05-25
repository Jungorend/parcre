from random import randint
from functools import reduce
from configuration import Config as CONFIG

startingClasses = {
    'worker': {
        'funds': [0,100000],
        'skills': ['craftsman','teacher','doctor','driver','cashier','farmer']
    },
    'investor': {
        'funds': [1000000000,100000000000],
        'skills': []
    }
}

requirements = {
    'minimum': ['food', 'food', 'regular clothing'],
    'farmer': [5]
}

class Person:
    def __init__(self,  soclass="", skills=[]):
        self.bankAccount = []
        self.job = []
        self.skills = skills
        if soclass == "":
            x = randint(0,200)
            if x < 3:
                self.soclass = 'investor'
                self.companies = []
            else:
                self.soclass = 'worker'
        else:
            self.soclass = soclass

    def setInitialFunds(self):
        return randint(startingClasses[self.soclass]['funds'][0], startingClasses[self.soclass]['funds'][1])

    def livingWages(self, city):
        # Certain skills require more regular expenses. This'll be representative
        # of the expectations for higher pay from them, or perhaps any dbets from training
        # Will expect the best requirements of the jobs they are skilled at, unless money is tight
        x = map(city.marketAverage, requirements['minimum'])
        minimumExpectedWage = reduce(lambda x,y: x + y, x)
        if city.banks[self.bankAccount[0]].displayFunds(self.bankAccount[1]) < minimumExpectedWage * CONFIG.povertyLine:
            return minimumExpectedWage
        additionalRequirements = 0
        for skill in self.skills:
            x = reduce(city.marketAverage, requirements[skill])
            if x > additionalRequirements:
                additionalRequirements = x
        return minimumExpectedWage + additionalRequirements

    def applyForJob(self, city):
        # Right now people will only apply for one job
        if self.job:
            return
        bestJobOffer = []
        minimumAcceptableWages = self.livingWages(city)
        for posting in city.getJobPostings():
            if posting[1].position in self.skills and posting[1].wages >= minimumAcceptableWages:
                if not bestJobOffer or bestJobOffer[1].wages < posting[1].wages:
                    bestJobOffer = posting
        if bestJobOffer:
            city.jobApply(self, bestJobOffer)

    def update(self,city,ticker):
        if ticker % CONFIG.jobSearchRate == 0:
            self.applyForJob(city)

