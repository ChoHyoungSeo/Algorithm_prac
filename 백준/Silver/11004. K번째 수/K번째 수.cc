#include <iostream>
#include <vector>
using namespace std;

void quickSort(vector<int> &A, int S, int E, int K);
int partition(vector<int> &A, int S, int E);
void swap(vector<int> &A, int i, int j);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, k;
    cin >> n >> k;
    vector<int> A(n);

    for (int i = 0; i<n; ++i){
        cin >> A[i];
    }
    quickSort(A, 0, n-1, k-1);
    cout << A[k-1];
}

void quickSort(vector<int> &A, int S, int E, int K){
    int pivot = partition(A, S, E);
    if (pivot == K){
        return;
    }
    else if (K < pivot){
        quickSort(A, S, pivot-1, K);
    }
    else{
        quickSort(A, pivot+1, E, K);
    }
}

int partition(vector<int> &A, int S, int E){
    if (S+1 == E){
        if (A[S] > A[E]){
            swap(A, S, E);
        }
        return E;
    }
    int M = (S+E) / 2;
    swap(A, S, M);
    int pivot = A[S];
    int i = S+1, j = E;
    while (i<=j){
        while (pivot < A[j] && j>0){
            j--;
        }
        while (pivot > A[i] && i < A.size()-1){
            i++;
        }
        if (i<=j){
            swap(A, i++, j--);
        }
    }
    A[S] = A[j];
    A[j] = pivot;
    return j;
}

void swap(vector<int> &A, int i, int j){
    int temp = A[i];
    A[i] = A[j];
    A[j] = temp;
}

// #include <iostream>
// #include <vector>
// #include <algorithm>
// using namespace std;

// int main() {
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr);

//     int n, k;
//     cin >> n >> k;
//     vector<int> arr(n);

//     // 배열 입력
//     for (int i = 0; i < n; ++i) {
//         cin >> arr[i];
//     }

//     sort(arr.begin(), arr.end());

//     cout << arr[k - 1] << "\n";

//     return 0;
// }