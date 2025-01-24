#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int n, m;
  cin >> n >> m;

  vector<long> prefixsum(n+1, 0);
  vector<long> modcnt(m, 0);

  for (int i = 1; i <= n; i++){
    int num;
    cin >> num;
    prefixsum[i] = prefixsum[i-1] + num;
    modcnt[prefixsum[i] % m]++;
  }

  long result = modcnt[0];
  for (int i = 0; i < m; i++){
    if (modcnt[i] > 1){
      result += (modcnt[i] * (modcnt[i]-1)) / 2;
    }
  }

  cout << result <<"\n";
  return 0;
  
}