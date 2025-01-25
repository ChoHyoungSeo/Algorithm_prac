#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main(){
  int s, p;
  string DNA;
  vector<int> required(4);
  vector<int> current(4,0);
  int validCnt = 0;
  
  cin >> s >> p;
  cin >> DNA;

  for (int i = 0; i < 4; i++){
    cin >> required[i];
  }

  for (int i = 0; i < p; i++){
    switch (DNA[i]){
      case 'A': current[0]++; break;
      case 'C': current[1]++; break;
      case 'G': current[2]++; break;
      case 'T': current[3]++; break;

    }
  }

  bool isValid = true;
  for (int i = 0; i < 4; i++){
    if (current[i] < required[i]){
      isValid = false;
      break;
    }
  }
  if (isValid) validCnt++;

  for (int i = p; i < s; i++){
    switch (DNA[i - p]){
      case 'A': current[0]--; break;
      case 'C': current[1]--; break;
      case 'G': current[2]--; break;
      case 'T': current[3]--; break;
    }

    switch (DNA[i]){
      case 'A': current[0]++; break;
      case 'C': current[1]++; break;
      case 'G': current[2]++; break;
      case 'T': current[3]++; break;
    }

    isValid = true;
    for (int j = 0; j < 4; j++){
      if (current[j] < required[j]){
        isValid = false;
        break;
      }
    }
    if (isValid) validCnt++;
  }

  cout << validCnt << "\n";

  return 0;
}
