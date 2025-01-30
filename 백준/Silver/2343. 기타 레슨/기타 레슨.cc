#include <iostream>
#include <vector>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    int start = 0, end = 0;
    
    for (int i = 0; i<n; i++){
        cin >> arr[i];
        if (start < arr[i]){
            start = arr[i];
        }
        end = end + arr[i];
    }

    while (start <= end){
        int middle = (start + end)/2;
        int sum = 0, count = 0;

        for (int i = 0; i < n; i++){
            if (sum + arr[i] > middle){
                count++;
                sum = 0;
            }
            sum = sum + arr[i];
        }
        if (sum != 0){
            count++;
        }
        if (count > m){
            start = middle+1;
        }
        else{
            end = middle-1;
        }
    }

    cout << start << "\n";
    
    return 0;
}