#include <fstream>
#include <iostream>
#include <sstream>
#include <unordered_map>
#include <vector>

using namespace std;

int main() {
  vector<int> col1, col2;

  // what is cool right away is that all the DSs are not there if we dont need
  // them... makes sense that this really helps us optimize memory
  // design principle of "you only pay for what you use"
  unordered_map<int, int> col2_hash;

  ifstream file("input.txt");

  if (!file.is_open()) {
    cerr << "Error opening file!" << endl;
    return 1;
  }

  string line;
  while (getline(file, line)) {
    // what is this?
    istringstream iss(line);
    int v1, v2;

    if (iss >> v1 >> v2) {
      col1.push_back(v1);
      col2.push_back(v2);
    }
  }

  file.close();
  // c++ way of saying give me each element in the container
  for (int v : col2) {
    col2_hash[v]++;
  }

  long long total = 0;
  for (int v : col1) {
    total += v * col2_hash[v];
  }

  cout << total << endl;

  return 0;
}
