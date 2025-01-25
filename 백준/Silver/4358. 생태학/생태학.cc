#include <iostream>
#include <map>
#include <string>
#include <iomanip>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  map<string, int> tree_cnt;
  string tree;
  int total = 0;

  while (getline(cin, tree)){
  if (tree.empty()) break;
  tree_cnt[tree]++;
  total++;
  }

  for (const auto& pair : tree_cnt){
    string tree_name = pair.first;
    int cnt = pair.second;
    double percentage = (cnt * 100.0) / total;
    cout << tree_name << " " << fixed << setprecision(4) << percentage << "\n";
  }
  
  return 0;
}