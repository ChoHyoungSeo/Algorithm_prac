#include <iostream>
#include <queue>

using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(NULL); cout.tie(NULL);

  int n;
  cin >> n;

  priority_queue<int> maxHeap;

  for (int i = 0; i < n; i++){
    int m;
    cin >> m;
    
    if (m > 0){
      maxHeap.push(m);
    }
    else{
      if (!maxHeap.empty()){
        cout << maxHeap.top() << "\n";
        maxHeap.pop();
      }
      else{
        cout << 0 << "\n";
      }
    }
  }
}