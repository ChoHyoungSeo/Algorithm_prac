#include <iostream>

int main() {
  int hour, minute, dur;
  std::cin >> hour >> minute >> dur;
  minute += dur;
  while (minute >= 60){
    minute -= 60;
    hour += 1;
    hour = (hour == 24) ? 0 : hour;
  }
  std::cout << hour << " " << minute << std::endl;
  return 0;
}