#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int test_case = 1; test_case <= T; ++test_case) {
        cout << "#" << test_case << " ";
        int N;
        cin >> N;

        priority_queue<int> max_heap;

        for (int i = 0; i < N; ++i) {
            int operation;
            cin >> operation;

            if (operation == 1) {
                int value;
                cin >> value;
                max_heap.push(value);
            } else if (operation == 2) {
                if (!max_heap.empty()) {
                    cout << max_heap.top() << " ";
                    max_heap.pop();
                } else {
                    cout << -1 << " ";
                }
            }
        }
        cout << "\n";
    }
    return 0;
}
