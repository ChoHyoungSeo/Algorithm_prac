#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int n, m;
  cin >> n >> m;

  unordered_map<string, int> name_to_number;
  vector<string> number_to_name(n+1);

  for (int i = 1; i <= n; i++){
    string name;
    cin >> name;
    name_to_number[name] = i;
    number_to_name[i] = name;
  }

  for (int i = 0; i < m; ++i){
    string query;
    cin >> query;

    if (isdigit(query[0])){
      int number = stoi(query);
      cout << number_to_name[number] <<"\n";
    }
    else{
      cout << name_to_number[query] << "\n";
    }
  }
  return 0;
}