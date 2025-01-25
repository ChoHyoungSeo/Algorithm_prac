#include <iostream>
#include <vector>
#include <queue>
using namespace std;

void findParents(vector<vector<int>>& tree, vector<int>& parents){
    queue<int> q;
    q.push(1);
    parents[1] = 0;

    while (!q.empty()){
        int current = q.front();
        q.pop();

        for (auto& next : tree[current]){
            if (parents[next] == 0){
                parents[next] = current;
                q.push(next);
            }
        }
    }
}

int main(){
    int n;
    cin >> n;

    vector<vector<int>> tree(n+1);
    vector<int> parents(n+1, 0);

    for (int i = 0; i < n - 1; ++i){
        int u, v;
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }

    findParents(tree, parents);

    for (int i = 2; i <= n; ++i){
        cout << parents[i] << "\n";
    }

    return 0;
}