#include <iostream>
#include <vector>
#include <cmath>

using namespace std;
typedef long long ll;

vector<ll> getPrimes(ll limit) {
    vector<bool> isPrime(limit + 1, true);
    vector<ll> primes;
    
    isPrime[0] = isPrime[1] = false;
    for (ll i = 2; i <= limit; i++) {
        if (isPrime[i]) {
            primes.push_back(i);
            for (ll j = i * i; j <= limit; j += i)
                isPrime[j] = false;
        }
    }
    return primes;
}

int main() {
    ll A, B;
    cin >> A >> B;
    
    vector<ll> primes = getPrimes(sqrt(B));
    
    int count = 0;
    
    for (ll prime : primes) {
        ll num = prime * prime;
        while (num <= B) {
            if (num >= A) count++;
            if (num > B / prime) break; //consider overflow
            num *= prime;
        }
    }
    
    cout << count << endl;
    return 0;
}
