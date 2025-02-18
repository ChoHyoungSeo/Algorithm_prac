#include <iostream>
#include <queue>
#include <vector>
using namespace std;

vector<int> visited;
int bfs(int node, vector<int>& visited);
vector<vector<int>> graph;
vector<int> ans;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m;
    cin >> n >> m;

    graph.resize(n+1);
    visited.resize(n+1, 0);
    ans.resize(n+1, 0);

    for(int i=0; i<m; ++i){
        int a, b;
        cin >> a >> b;
        graph[b].push_back(a);
    }
    
    int maxNum = -1;
    for (int i=1; i<=n; ++i){
        fill(visited.begin(), visited.end(), 0);
        int cnt = bfs(i, visited);
        if (maxNum < cnt){
            maxNum = cnt;
        }
        ans[i] = cnt;
    }
    
    for(int i = 0; i < ans.size(); ++i){
        if (maxNum == ans[i]){
            cout << i << " ";
        }
    }

    return 0;
}

int bfs(int node, vector<int>& visited){
    queue<int> q;
    q.push(node);
    visited[node] = 1;
    int cnt = 0;

    while(!q.empty()){
        int now;
        now = q.front();
        q.pop();
        for (int i : graph[now]){
            if (visited[i] == 0){
                q.push(i);
                visited[i] = 1;
                cnt++;
            }
        }
    }
    return cnt;
}