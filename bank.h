#ifndef BANK_H
#define BANK_H

class BankAccount {
public:
  int accountNumber;
  int funds;
  BankAccount(int aNumber);
};

class Bank {
private:
  int numOfAccounts;
  int currentID;
  BankAccount **bankAccount;

public:
  Bank();
  ~Bank();

  int createAccount();
  int displayFunds(int aNumber);
  void addFunds(int aNumber, int funds);
};

#endif
