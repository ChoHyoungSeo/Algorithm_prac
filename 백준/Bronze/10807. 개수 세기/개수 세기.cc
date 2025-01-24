#include <iostream>
#include <vector>
using namespace std;

int main(){
  int tot, tmp, tar, ans = 0;
  vector<int> nums;
  cin >> tot;

  for (int i = 0; i < tot; i++){
    cin >> tmp;
    nums.push_back(tmp);
  }
  cin >> tar;

  for (int i = 0; i < tot; i++){
    if (nums[i] == tar){
      ans += 1;
    }
  }
  cout << ans <<"\n";
  return 0;
}