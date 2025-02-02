#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int m, n;
    cin >> m >> n;
    vector<int> prime(n+1);

    for (int i = 2; i<=n; i++){
        prime[i] = i;
    }

    for (int i = 2; i<=sqrt(n); i++){
        if (prime[i] == 0){
            continue;
        }
        for (int j = i+i; j<=n; j=j+i){
            prime[j] = 0;
        }
    }
    for (int i = m; i<=n; i++){
        if (prime[i] != 0){
            cout << prime[i] << "\n";
        }
    }
    return 0;
}