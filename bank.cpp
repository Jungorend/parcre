#include "config.h"
#include "bank.h"

BankAccount::BankAccount(int aNumber) {
  accountNumber = aNumber;
  funds = 0;
}

// Current ID is for the next account in line. If accounts get
// removed, this will ensure people can keep their account number.
// but never more than maxAccounts at a time
Bank::Bank() {
  numOfAccounts = 0;
  currentID = 0;
  bankAccount = new BankAccount*[config::maxAccounts];
}

Bank::~Bank() {
  for(int i=0; i < numOfAccounts; i++)
    delete bankAccount[i];
  delete []bankAccount;
}

int Bank::createAccount() {
  if(numOfAccounts >= config::maxAccounts)
    return -1;
  bankAccount[numOfAccounts] = new BankAccount(currentID);
  currentID++;
  return numOfAccounts++;
}

// TODO:: This needs a hashmap or similar eventually so that when
// account numbers =/= the index it'll still find them in O(1) time.
int Bank::displayFunds(int aNumber) {
  return bankAccount[aNumber]->funds;
}

//TODO: Eventually design this into a credit/debit transaction
// to ensure all money is kept stable potentially?
void Bank::addFunds(int aNumber, int funds) {
  bankAccount[aNumber]->funds = funds;
}
