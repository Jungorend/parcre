from parcre.city import City
from parcre.company import Company


c = City()
for i in range(1000):
    c.update()

def test():
    assert(type(c.getJobPostings()[0][1].wages) == int)

