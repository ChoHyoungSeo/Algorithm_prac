#include <iostream>
#include <queue>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cout.tie(nullptr);

  int n;
  cin >> n;
  priority_queue<int> positivePq;
  priority_queue<int, vector<int>, greater<int>> negativePq;
  int one = 0, zero = 0;

  for (int i = 0; i < n; i++){
    int data;
    cin >> data;
    if (data > 1){
      positivePq.push(data);
    }
    else if (data == 1){
      one++;
    }
    else if (data == 0){
      zero++;
    }
    else{
      negativePq.push(data);
    }
  }

  int sum = 0;

  while (positivePq.size() > 1){
    int first = positivePq.top();
    positivePq.pop();
    int second = positivePq.top();
    positivePq.pop();
    sum = sum + first * second;
  }
  if (!positivePq.empty()){
    sum = sum + positivePq.top();
    positivePq.pop();
  }

  while(negativePq.size() > 1){
    int first = negativePq.top();
    negativePq.pop();
    int second = negativePq.top();
    negativePq.pop();
    sum = sum + first * second;
  }
  if (!negativePq.empty()){
    if(zero == 0){
      sum = sum + negativePq.top();
      negativePq.pop();
    }
  }
  sum = sum + one;
  cout << sum;
  return 0;
}