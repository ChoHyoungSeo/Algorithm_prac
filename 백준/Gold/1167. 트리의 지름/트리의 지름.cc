#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int MAX = 100001;
vector<pair<int, int>> tree[MAX];
bool visited[MAX];
int maxDist=0, farthestNode=0;

void dfs(int node, int dist){
    if (visited[node]) return;
    visited[node] = true;

    if (dist > maxDist){
        maxDist = dist;
        farthestNode = node;
    }

    for (auto &next: tree[node]){
        int nextNode = next.first;
        int nextDist = next.second;
        dfs(nextNode, dist+nextDist);
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int V;
    cin >> V;

    for (int i = 0; i<V; i++){
        int node;
        cin >> node;

        while (true){
            int adj, cost;
            cin >> adj;
            if (adj==-1) break;
            cin >> cost;
            tree[node].push_back({adj, cost});
            tree[adj].push_back({node, cost});
        }
    }

    memset(visited, false, sizeof(visited));
    dfs(1,0);

    memset(visited, false, sizeof(visited));
    maxDist=0;
    dfs(farthestNode, 0);

    cout << maxDist << "\n";
    return 0;
}