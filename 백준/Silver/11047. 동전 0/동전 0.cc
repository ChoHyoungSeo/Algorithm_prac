#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n, k;
  cin >> n >> k;
  vector<int> coin(n);

  for (int i=0; i<n; i++){
    cin >> coin[i];
  }

  int cnt = 0;

  for (int i = n-1; i>=0; i--){
    if(coin[i] <= k){
      cnt += (k/coin[i]);
      k = k%coin[i];
    }
  }

  cout << cnt << "\n";
}