#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int n;
    cin >> n;
    vector<pair<int, int>> v(n);

    for (int i = 0; i<n; i++){
        cin >> v[i].second;
        cin >> v[i].first;
    }
    sort(v.begin(), v.end());

    int cnt = 0, end = -1;

    for (int i = 0; i < n; i++){
        if (v[i].second >= end){
            end = v[i].first;
            cnt++;
        }
    }
    cout << cnt;
    return 0;
}