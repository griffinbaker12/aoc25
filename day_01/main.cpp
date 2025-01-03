#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <string>
#include <vector>

int main() {
  std::ifstream in{"input.txt"};
  if (!in) {
    return 1;
  }

  std::vector<int> c1, c2;
  int n1, n2;
  while (in >> n1 >> n2) {
    c1.push_back(n1);
    c2.push_back(n2);
  }

  std::sort(c1.begin(), c1.end());
  std::sort(c2.begin(), c2.end());

  int total{0};
  for (auto [n1, n2] : std::views::zip(c1, c2)) {
    total += abs(n2 - n1);
  }

  std::cout << total << std::endl;

  return 0;
}
