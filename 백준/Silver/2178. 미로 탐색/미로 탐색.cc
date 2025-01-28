#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, m;
vector<vector<int>> maze;
vector<vector<int>> visited;
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

int bfs(int startX, int startY){
    queue<pair<int, int>> q;
    q.push({startX, startY});
    visited[startX][startY] = 1;

    while (!q.empty()){
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int i = 0; i<4; ++i){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (nx >= 0 && nx < n && ny >= 0 && ny < m){
                if (!visited[nx][ny] && maze[nx][ny] == 1){
                    visited[nx][ny] = visited[x][y] + 1;
                    q.push({nx, ny});
                }
            }
        }
    }

    return visited[n-1][m-1];
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m;
    maze.resize(n, vector<int>(m));
    visited.resize(n, vector<int>(m,0));

    for (int i = 0; i<n; ++i){
        string line;
        cin >> line;
        for (int j = 0; j<m; ++j){
            maze[i][j] = line[j] - '0';
        }
    }

    cout << bfs(0,0) << "\n";
    return 0;
}