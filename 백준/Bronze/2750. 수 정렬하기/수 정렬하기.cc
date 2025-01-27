#include <iostream>
#include <vector>
using namespace std;

void bubbleSort(vector<int>& arr){
    int n = arr.size();
    for (int i = 0; i<n; ++i){
        bool swapped = false;
        for (int j = 0; j < n-1-i; ++j){
            if (arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);

    int n;
    cin >> n;
    vector<int> arr(n);

    for (int i = 0; i<n; i++){
        cin >> arr[i];
    }
    bubbleSort(arr);

    for (auto& num : arr){
        cout << num <<"\n";
    }

    return 0;
}

// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(0);

//     int n;
//     cin >> n;
//     vector<int> arr(n);

//     for (int i = 0; i<n; ++i){
//         arr[i] = i+1;
//     }

//     sort(arr.begin(), arr.end());

//     for (auto& num : arr){
//         cout << num << "\n";
//     }

//     return 0;
// }