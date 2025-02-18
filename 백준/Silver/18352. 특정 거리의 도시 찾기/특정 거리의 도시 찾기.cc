#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

void bfs(int node);
vector<vector<int>> graph;
vector<int> visited;
vector<int> ans;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int n, m, k, x;
    cin >> n >> m >> k >> x;

    visited.resize(n+1,0);
    graph.resize(n+1);
    
    for(int i=0; i<m; ++i){
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
    }
    
    bfs(x);

    for(int i=0; i<visited.size(); ++i){
        if (visited[i] == k+1){
            ans.push_back(i);
        }
    }
    if (!ans.empty()){
        sort(ans.begin(), ans.end());
        for(int i=0; i < ans.size(); ++i){
            cout << ans[i] << "\n";
        }
    } else{
        cout << "-1" << "\n";
    }

    return 0;
}

void bfs(int node){
    queue<int> q;
    q.push(node);
    visited[node]++;

    while(!q.empty()){
        int now = q.front();
        q.pop();
        for (int i : graph[now]){
            if (visited[i] == 0){
                visited[i] = visited[now]+1;
                q.push(i);
            }
        }
        
    }
}
