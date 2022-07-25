#include <iostream>
#include <algorithm>
#include <vector>

int main() {
  int a, b, c;
  std::cin >> a >> b >> c;
  std::vector <int> nums = {a, b, c};
  
  if ((a == b) & (a == c)){
    std::cout << 10000+a*1000 << std::endl;
  }
  else if ((a == b & a != c) | (a != b & a== c)){
    std::cout << 1000+a*100 << std::endl;
  }
  else if ((b != a) & (b == c) & (a != c)){
    std::cout << 1000+b*100 << std::endl;
  }
  else{
    sort(nums.begin(), nums.end());
    std::cout << nums.back()*100 << std::endl;
  }
  return 0;
}