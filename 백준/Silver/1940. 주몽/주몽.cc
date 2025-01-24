#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);

  int n, m;
  cin >> n >> m;
  vector<int> v(n,0);

  for (int i = 0; i < n; i++){
    cin >> v[i];
  }
  
  sort(v.begin(), v.end());
  
  int cnt = 0, i = 0;
  int j = n-1;
  while (i < j){
    if (v[i] + v[j] < m){
      i++;
    }
    else if (v[i] + v[j] > m){
      j--;
    }
    else{
      cnt++;
      i++;
      j--;
    }
  }
  cout << cnt << "\n";
  return 0;
}