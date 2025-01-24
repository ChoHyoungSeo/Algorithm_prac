#include <iostream>
using namespace std;

int main(){
  int tot, max = 0;
  int arr[1000];
  int sum = 0;
  
  cin >> tot;
  
  for (int i = 0; i < tot; i++){
    cin >> arr[i];
  }
  for (int i = 0; i < tot; i++){
    if (arr[i] > max){
      max = arr[i];
    }
    sum += arr[i];
  }

  float ans = sum * 100.0 / max / tot;
  cout << ans << "\n";
  
}