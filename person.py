from random import randint

startingClasses = {
    'worker': {
        'funds': [0,100000],
        'skills': ['craftsman','teacher','doctor','driver','cashier']
    },
    'investor': {
        'funds': [1000000000,100000000000],
        'skills': ['employer','investor','influencer']
    }
}

class Person:
    def __init__(self, soclass=""):
        self.bankAccount = []
        self.job = []
        if soclass == "":
            x = randint(0,200)
            if x < 3:
                self.soclass = 'investor'
            else:
                self.soclass = 'worker'
        else:
            self.soclass = soclass

    def setInitialFunds(self):
        return randint(startingClasses[self.soclass]['funds'][0], startingClasses[self.soclass]['funds'][1])

