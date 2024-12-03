#include <iostream>
#include <vector>

using namespace std;

int main() {
  int size = 1000;
  vector<int> vals;
  for (int i = 0; i < size; i++) {
    vals.push_back(i);
  }
  for (int v : vals) {
    cout << v << endl;
  }
  return 0;
}
