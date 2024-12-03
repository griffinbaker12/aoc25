#include <iostream>
#include <string>

using namespace std;

int main() {
  string name;
  cout << "What's your name? ";
  getline(std::cin, name);
  cout << "Hello, " << name << "!" << std::endl;
  return 0;
}
