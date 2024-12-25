#include <cstdlib>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <vector>

using namespace std;

int main() {
  fstream in{"input.txt"};
  if (!in) return 1;

  int total = 0;
  string line;
  while (getline(in, line)) {
    istringstream iss(line);
    vector<int> sequence{istream_iterator<int>(iss), istream_iterator<int>()};
    int incr = sequence[1] - sequence[0];
    bool safe = true;
    for (auto [n1, n2] : views::zip(sequence, sequence | views::drop(1))) {
      cout << "n1 " << n1 << " n2 " << n2 << endl;
      int diff = n2 - n1;
      if (abs(diff) < 1 || abs(diff) > 3 or (incr * diff) <= 0) {
        safe = false;
        break;
      }
    }
    cout << "safe: " << safe << endl;
    if (safe) total++;
  }
  cout << total << endl;
  return 0;
}
