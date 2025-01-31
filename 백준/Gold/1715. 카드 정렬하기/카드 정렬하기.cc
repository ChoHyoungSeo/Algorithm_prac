#include <iostream>
#include <queue>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n;
  cin >> n;
  priority_queue<int, vector<int>, greater<int>> pq;
  
  for (int i = 0; i < n; i++){
    int x;
    cin >> x;
    pq.push(x);
  }
  
  int total_cost = 0;

  while (pq.size() > 1){
    int first = pq.top(); pq.pop();
    int second = pq.top(); pq.pop();

    int cost = first + second;
    total_cost += cost;

    pq.push(cost);
  }

  cout << total_cost << "\n";
  return 0;
}