#include <iostream>
#include <vector>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL);
  cout.tie(NULL);

  int n;
  cin >> n;
  vector<int> degree(n+1,0);

  for (int i = 0; i<n-1; i++){
    int a, b;
    cin >> a >> b;
    degree[a]++;
    degree[b]++;
  }

  int q;
  cin >> q;

  while (q--){
    int t, k;
    cin >> t >> k;

    if (t == 1){
      if (degree[k] > 1){
        cout << "yes\n";
      } else{
        cout << "no\n";
      }
    } else{
      cout << "yes\n";
    }
  }

  return 0;
}