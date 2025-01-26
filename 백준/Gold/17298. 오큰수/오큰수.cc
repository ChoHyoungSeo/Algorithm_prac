#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n;
    cin >> n;
    vector<int> arr(n);
    vector<int> ans(n, -1);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }

    stack<int> myStack;
    myStack.push(0);

    for (int i = 1; i < n; i++){
        while (!myStack.empty() && arr[myStack.top()] < arr[i]){
            ans[myStack.top()] = arr[i];
            myStack.pop();
        }
        myStack.push(i);
    }

    for (auto& answer : ans){
        cout << answer << " ";
    }

    return 0;
}