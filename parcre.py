from bank import Bank
from person import Person
from city import City
from company import Company

if __name__ == "__main__":
    c = City()
    c.companies[0].update()
    c.companies[0].update()
    c.companies[0].update()
    c.companies[0].update()
    c.companies[0].update()
    for x in c.getJobPostings():
        print("{} {}\n".format(x[1].position, x[1].wages))

