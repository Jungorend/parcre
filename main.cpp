#include <iostream>
#include "bank.h"
using std::cout, std::endl;


int main() {
  Bank bank;
  int x = bank.createAccount();
  int y = bank.createAccount();
  bank.addFunds(x, 1200);
  bank.addFunds(y, 500);
  cout << "You have an account, your id is: " << x << "." << endl;
  cout << "Current Funds are: " << bank.displayFunds(x) << "." << endl;
  cout << "------------" << endl;
  cout << "You have an account, your id is: " << y << "." << endl;
  cout << "Current Funds are: " << bank.displayFunds(y) << "." << endl;
  return 0;
}
