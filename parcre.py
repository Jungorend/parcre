from parcre.bank import Bank
from parcre.person import Person
from parcre.city import City
from parcre.company import Company

if __name__ == "__main__":
    c = City()
    for i in range(1000):
        c.update()
    for x in c.getJobPostings():
        print("{} {}|".format(x[1].position, x[1].wages))
