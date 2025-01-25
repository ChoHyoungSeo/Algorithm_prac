#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
  ios::sync_with_stdio(false);
  cin.tie(0); cout.tie(0);

  int n;
  cin >> n;
  vector<int> v(n,0);

  for(int i = 0; i < n; i++){
    cin >> v[i];
  }

  sort(v.begin(), v.end());
  int result = 0;
  for (int i = 0; i < n; i++){
    long target = v[i];
    int j = 0;
    int k = n-1;

    while(j < k){
      if(v[j] + v[k] == target){
        if (j != i && k != i){
          result++;
          break;
        }
        else if (i == j){
          j++;
        }
        else if(k == i){
          k--;
        }
      }
      else if (v[j] + v[k] < target){
        j++;
      }
      else{
        k--;
      }
    }
  }
  cout << result <<"\n";
  return 0;
}