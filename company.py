from commodity import commodity_types

class Employee:
    def __init__(self, id, role, wages):
        self.id = id
        self.role = role
        self.wages = wages

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

    # Determine best product will look at market factors to determine what
    # the company should produce, and can be used for staffing decisions accordingly
    # This may need to be outside the company class and more based on what other
    # companies are doing as well
    def determineBestProduct(self):
        return 'food'

    # TODO: sets price based on existing hiring postings, increasing over time if unsuccessful
    def setHiringPrice(self, deps):
        return 1

    # Non-destructive
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
                required_roles.append([deps, self.setHiringPrice(deps)])
        if required_roles == []:
            self.employees['assigned'].append(new_assignments)
            for e in new_assignments:
                self.employees['available'].remove(e)
        else:
            if expenses > (self.financing['bank'].displayFunds(self.financing['bankAccount']) - self.financing['budgeted']):
                return
            self.financing['budgeted'] += expenses
            self.jobPostings.extend(required_roles)





