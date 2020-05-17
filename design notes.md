# Current Design Notes

## City
The city is a global object that maintains the state of everything within for now. It has links to all the banks, people, and companies, and allows them to interoperate as a result by interacting with the city.

## Companies
Companies post their jobs internally. Down the road a company dedicated to recruting that gathers this may help but for now it's all maintained by the City class. Companies are owned by the person who founded them--no publically traded companies yet.

## People
Still not decided if these are individual people or an abstract concept of a group of people in a similar position. Will take time to decide. Broken up into workers who earn money to buy goods, and investors, who create companies to earn money.