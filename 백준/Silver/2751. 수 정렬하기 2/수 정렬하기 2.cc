#include <iostream>
#include <vector>
using namespace std;

void merge_sort(int s, int e);
static vector<int> arr;
static vector<int> tmp;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n;
    cin >> n;
    arr = vector<int>(n+1);
    tmp = vector<int>(n+1);

    for (int i = 1; i<=n; i++){
        cin >> arr[i];
    }
    merge_sort(1, n);

    for (int i = 1; i<=n; i++){
        cout << arr[i] << "\n";
    }
}

void merge_sort(int s, int e){
    if (e-s < 1){
        return;
    }
    int m = s+(e-s) / 2;
    merge_sort(s, m);
    merge_sort(m+1, e);

    for (int i = s; i<=e; i++){
        tmp[i] = arr[i];
    }

    int k = s;
    int index1 = s;
    int index2 = m+1;

    while (index1 <= m && index2 <= e){
        if (tmp[index1] > tmp[index2]){
            arr[k] = tmp[index2];
            k++;
            index2++;
        }
        else{
            arr[k] = tmp[index1];
            k++;
            index1++;
        }
    }

    while (index1 <= m){
        arr[k] = tmp[index1];
        k++;
        index1++;
    }
    while (index2 <= e){
        arr[k] = tmp[index2];
        k++;
        index2++;
    }
}