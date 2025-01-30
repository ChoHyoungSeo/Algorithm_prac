#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n, m;
    cin >> n;
    vector<int> arr(n);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    cin >> m;

    for (int i = 0; i<m; i++){
        bool find = false;
        int target;
        cin >> target;
        int start = 0;
        int end = arr.size() - 1;

        while (start <= end){
            int mididx = (start+end)/2;
            int midval = arr[mididx];

            if (midval > target){
                end = mididx-1;
            }
            else if (midval < target){
                start = mididx+1;
            }
            else {
                find = true;
                break;
            }
        }
        if (find){
            cout << 1 << "\n";
        }
        else{
            cout << 0 << "\n";
        }
    }

    return 0;
}