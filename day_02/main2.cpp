#include <cstdlib>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <vector>

using namespace std;

bool is_safe(const vector<int>& sequence) {
  int incr = sequence[1] - sequence[0];
  bool safe = true;
  for (auto [n1, n2] : views::zip(sequence, sequence | views::drop(1))) {
    int diff = n2 - n1;
    if (abs(diff) < 1 || abs(diff) > 3 or (incr * diff) <= 0) {
      safe = false;
      break;
    }
  }
  return safe;
}

int main() {
  fstream in{"input.txt"};
  if (!in) return 1;

  int total = 0;
  string line;
  while (getline(in, line)) {
    istringstream iss(line);
    // creates sequence from beginning to the end
    vector<int> sequence{istream_iterator<int>(iss), istream_iterator<int>()};
    bool safe = is_safe(sequence);
    if (safe)
      total++;
    else {
      for (size_t i = 0; i < sequence.size(); i++) {
        vector<int> modified = sequence;
        modified.erase(modified.begin() + i);

        if (is_safe(modified)) {
          safe = true;
          break;
        }
      }
      if (safe) total++;
    }
  }
  cout << total << endl;
  return 0;
}
