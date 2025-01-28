//counting sort
#include <iostream>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;
    int count[10001] = {0};
    int number = 0;

    for (int i = 1; i<=n; i++){
        cin >> number;
        count[number]++;
    }
    for (int i = 0; i<= 10000; i++){
        if (count[i] != 0){
            for (int j= 0; j < count[i]; j++){
                cout << i <<"\n";
            }
        }
    }
}