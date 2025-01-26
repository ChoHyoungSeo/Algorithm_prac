#include <iostream>
#include <queue>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    queue<int> myQueue;
    int n;
    cin >> n;

    for (int i = 1; i <= n; i++){
        myQueue.push(i);
    }
    while (myQueue.size() > 1){
        myQueue.pop();
        myQueue.push(myQueue.front());
        myQueue.pop();
    }
    cout << myQueue.front() << "\n";

    return 0;
}