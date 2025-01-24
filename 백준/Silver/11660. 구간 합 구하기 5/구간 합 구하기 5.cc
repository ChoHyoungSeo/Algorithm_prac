#include <iostream>
#include <vector>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> graph(n + 1, vector<int>(n + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int tmp;
            cin >> tmp;
            graph[i][j] = tmp + graph[i-1][j] + graph[i][j-1] - graph[i-1][j-1];
        }
    }

    for (int i = 0; i < m; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        cout << graph[x2][y2] - graph[x1-1][y2] - graph[x2][y1-1] + graph[x1-1][y1-1] << "\n";
    }

    return 0;
}
