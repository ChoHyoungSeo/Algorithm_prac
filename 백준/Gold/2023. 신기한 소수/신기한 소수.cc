#include <iostream>
#include <cmath>
using namespace std;

bool isPrime(int num) {
    if (num < 2) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}

void findAmazingPrimes(int currentNum, int currentLength, int targetLength) {
    if (currentLength == targetLength) {
        cout << currentNum << '\n';
        return;
    }

    for (int i = 1; i <= 9; i++) {
        int nextNum = currentNum * 10 + i;
        if (isPrime(nextNum)) {
            findAmazingPrimes(nextNum, currentLength + 1, targetLength);
        }
    }
}

int main() {
    int N;
    cin >> N;

    for (int prime : {2, 3, 5, 7}) {
        findAmazingPrimes(prime, 1, N);
    }

    return 0;
}


// #include <iostream>
// using namespace std;

// void DFS(int number, int digits);
// bool isPrime(int num);
// static int n;

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr); cout.tie(nullptr);

//     cin >> n;
//     DFS(2, 1);
//     DFS(3, 1);
//     DFS(5, 1);
//     DFS(7, 1);
// }

// void DFS(int number, int digits){
//     if (digits == n){
//         if (isPrime(number)){
//             cout << number << "\n";
//         }

//         return;
//     }
//     for (int i = 0; i<10; i++){
//         if (i%2 == 0){
//             continue;
//         }
//         if (isPrime(number*10+i)){
//             DFS(number*10 + i, digits+1);
//         }
//     }
// }

// bool isPrime(int num){
//     for (int i = 2; i<=num/2; i++){
//         if (num%i == 0){
//             return false;
//         }
//     }
//     return true;
// }