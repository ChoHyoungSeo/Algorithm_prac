//dfs.. O(V+E) -> 5000 100 OK..
#include <iostream>
#include <vector>

using namespace std;

vector<vector<int>> graph;
vector<int> visited;

void dfs(int node){
    visited[node] = true;

    for (int num : graph[node]){
        if (!visited[num]){
            dfs(num);
        }
    }
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);
    int tot;
    cin >> tot;
    
    for (int test_case=1; test_case <= tot; ++test_case){
        int n, m;
        cin >> n >> m;

        graph.assign(n+1, vector<int>());
        visited.assign(n+1, 0);
        
        for (int i=0; i<m; ++i){
            int person, target;
            cin >> person >> target;
            
            graph[person].push_back(target);
            graph[target].push_back(person);
        }
        
        int cnt = 0;
        
        for (int i=1; i<=n; ++i){
            if (visited[i] == 0){
                dfs(i);
                cnt++;
            }
        }
        cout << "#" << test_case << " " << cnt << "\n";
    }
    
    return 0;
}