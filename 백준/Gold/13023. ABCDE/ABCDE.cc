//DFS O(V+E),, 4000*2000 = 8000000,, OK
#include <iostream>
#include <vector>
using namespace std;

int n, m;
vector<vector<int>> adj;
vector<bool> visited;
bool found = false;
void DFS(int node, int depth);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> n >> m;
    adj.resize(n);
    visited.resize(n, false);

    for (int i = 0; i<m; i++){
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 0; i<n; i++){
        DFS(i, 0);
        if (found) break;
    }

    cout << (found ? 1 : 0) << "\n";
    return 0;
}

void DFS(int node, int depth){
    if (depth==4){
        found=true;
        return;
    }

    visited[node] = true;

    for (int neighbor : adj[node]){
        if (!visited[neighbor]){
            DFS(neighbor, depth+1);
            if (found) return;
        }
    }
    visited[node] = false; //backtracking
}