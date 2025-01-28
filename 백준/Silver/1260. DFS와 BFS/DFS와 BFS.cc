#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited);
void bfs(int start, vector<vector<int>>& graph, vector<bool>& visited);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    
    int n, m, start;
    cin >> n >> m >> start;

    vector<vector<int>> graph(n+1);
    vector<bool> visited(n+1, false);

    for (int i = 0; i<m; ++i){
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    for (int i = 1; i<=n; ++i){
        sort(graph[i].begin(), graph[i].end());
    }

    dfs(start, graph, visited);
    cout << "\n";

    fill(visited.begin(), visited.end(), false);
    bfs(start, graph, visited);

    return 0;
}

void dfs(int node, vector<vector<int>>& graph, vector<bool>& visited){
    visited[node]= true;
    cout << node << " ";

    for (int next: graph[node]){
        if (!visited[next]){
            dfs(next, graph, visited);
        }
    }
}

void bfs(int start, vector<vector<int>>& graph, vector<bool>& visited){
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()){
        int node = q.front();
        q.pop();
        cout << node << " ";

        for (int next: graph[node]){
            if (!visited[next]){
                visited[next] = true;
                q.push(next);
            }
        }
    }
}