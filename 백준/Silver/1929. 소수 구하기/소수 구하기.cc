#include <iostream>
#include <vector>
using namespace std;

void sieve(int m, int n) {
    vector<bool> is_prime(n + 1, true);
    is_prime[0] = is_prime[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (is_prime[i]) {
            for (int j = i * i; j <= n; j += i) { 
                is_prime[j] = false;
            }
        }
    }

    for (int i = m; i <= n; i++) {
        if (is_prime[i]) {
            cout << i << '\n';
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);

    int m, n;
    cin >> m >> n;

    sieve(m, n);

    return 0;
}


// #include <iostream>
// #include <vector>
// #include <cmath>
// using namespace std;

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(0); cout.tie(0);

//     int m, n;
//     cin >> m >> n;
//     vector<int> prime(n+1);

//     for (int i = 2; i<=n; i++){
//         prime[i] = i;
//     }

//     for (int i = 2; i<=sqrt(n); i++){
//         if (prime[i] == 0){
//             continue;
//         }
//         for (int j = i+i; j<=n; j=j+i){
//             prime[j] = 0;
//         }
//     }
//     for (int i = m; i<=n; i++){
//         if (prime[i] != 0){
//             cout << prime[i] << "\n";
//         }
//     }
//     return 0;
// }