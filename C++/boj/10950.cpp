#include <iostream>

int main() {
  int total, a, b;
  std::cin >> total;
  for(int i = 0; i < total; i++){
    std::cin >> a >> b;
    std::cout << a + b << std::endl;
  }
  return 0;
}