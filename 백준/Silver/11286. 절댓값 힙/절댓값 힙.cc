#include <iostream>
#include <queue>
#include <cmath>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int n;
  cin >> n;

  priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int, int>>> pq;

  for (int i = 0; i < n; ++i){
    int x;
    cin >> x;

    if (x == 0){
      if (pq.empty()){
        cout << 0 << "\n";
      } else{
        cout << pq.top().second << "\n";
        pq.pop();
      }
    } else{
      pq.push({abs(x), x});
    }
  }

  return 0;
}