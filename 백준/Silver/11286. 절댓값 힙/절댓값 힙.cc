#include <iostream>
#include <queue>
using namespace std;

struct compare {
    bool operator()(int o1, int o2){
        int first_abs = abs(o1);
        int second_abs = abs(o2);
        if (first_abs == second_abs){
            return o1 > o2;
        }
        else{
            return first_abs > second_abs;
        }
    }
};

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    priority_queue<int, vector<int>, compare> myQueue;

    int n;
    cin >> n;

    for (int i = 0; i < n; i++){
        int req;
        cin >> req;

        if (req == 0){
            if (myQueue.empty()){
                cout << "0\n";
            }
            else{
                cout << myQueue.top() << "\n";
                myQueue.pop();
            }
        }
        else{
            myQueue.push(req);
        }
    }
    return 0;
}

// #include <iostream>
// #include <queue>
// #include <cmath>

// using namespace std;

// int main(){
//   ios::sync_with_stdio(false);
//   cin.tie(0); cout.tie(0);

//   int n;
//   cin >> n;

//   priority_queue<pair<int, int>, vector<pair<int,int>>, greater<pair<int, int>>> pq;

//   for (int i = 0; i < n; ++i){
//     int x;
//     cin >> x;

//     if (x == 0){
//       if (pq.empty()){
//         cout << 0 << "\n";
//       } else{
//         cout << pq.top().second << "\n";
//         pq.pop();
//       }
//     } else{
//       pq.push({abs(x), x});
//     }
//   }

//   return 0;
// }