#include <algorithm>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <ranges>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
  std::ifstream in{"input.txt"};
  if (!in) {
    return 1;
  }

  // nice that this parses according to the type of variable we declare
  std::vector<int> c1, c2;
  int n1, n2;
  while (in >> n1 >> n2) {
    c1.push_back(n1);
    c2.push_back(n2);
  }

  // nice that this inits to 0
  std::unordered_map<int, int> frequencies;
  for (int n2 : c2) frequencies[n2]++;

  std::cout << std::transform_reduce(
                   c1.begin(), c1.end(), 0, std::plus<>{},
                   [&frequencies](int n) { return n * frequencies[n]; })
            << std::endl;

  return 0;
}
