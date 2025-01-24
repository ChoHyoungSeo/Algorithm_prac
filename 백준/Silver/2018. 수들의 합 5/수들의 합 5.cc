//10000000, O(nlogn) 안됨. O(n)
#include <iostream>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int num;
  cin >> num;
  int count = 1; //num == sum
  int start_index = 1, end_index = 1, sum = 1;

  while (end_index != num){
    if (sum == num){
      count++;
      end_index++;
      sum += end_index;
    }
    else if (sum > num){
      sum -= start_index;
      start_index++;
    }
    else{
      end_index++;
      sum += end_index;
    }
  }
  cout << count << "\n";
  return 0;
}