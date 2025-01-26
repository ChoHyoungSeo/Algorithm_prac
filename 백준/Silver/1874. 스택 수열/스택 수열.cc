#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    int n;
    cin >> n;

    vector<int> sequence(n);
    for (int i = 0; i < n; ++i){
        cin >> sequence[i];
    }

    stack<int> s;
    vector<string> operations;
    int current = 1;

    for (int i = 0; i < n; ++i){
        int target = sequence[i];

        while (current <= target){
            s.push(current);
            operations.push_back("+");
            ++current;
        }

        if (s.top() == target){
            s.pop();
            operations.push_back("-");
        } else{
            cout << "NO";
            return 0;
        }
    }

    for (const string& op : operations){
        cout << op <<"\n";
    }

    return 0;
}