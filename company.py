class Employee:
    def __init__(self, id, role, wages):
        self.id = id
        self.role = role
        self.wages = wages

class Company:
    def __init__(self, financeCapital, targetProduct=determineBestProduct()):
        self.account = financeCapital
        self.employees = []
        self.technologies = []
        self.targetProduct = targetProduct

    # Determine best product will look at market factors to determine what
    # the company should produce, and can be used for staffing decisions accordingly
    def determineBestProduct(self):
        return 'food'
