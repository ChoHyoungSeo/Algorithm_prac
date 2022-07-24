#include <iostream>

int main() {
  int hour, minute;
  std::cin >> hour >> minute;
  minute -= 45;
  if (minute < 0){
    minute += 60;
    hour = (hour == 0) ? 23 : hour-1;
  }
  std::cout << hour << " " << minute;
  return 0;
}