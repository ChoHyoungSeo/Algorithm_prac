#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int n;
  cin >> n;

  priority_queue<int, vector<int>, greater<int>> minHeap;

  for (int i = 0; i < n; ++i){
    for (int j = 0; j < n; ++j){
      int num;
      cin >> num;

      if (minHeap.size() < n){
        minHeap.push(num);
      }
      else if (num > minHeap.top()){
        minHeap.pop();
        minHeap.push(num);
      }
    }
  }
  cout << minHeap.top() << "\n";

  return 0;
}
