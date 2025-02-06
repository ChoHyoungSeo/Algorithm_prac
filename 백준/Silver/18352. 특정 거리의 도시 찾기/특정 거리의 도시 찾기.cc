#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int n, m, k, x;
vector<vector<int>> graph;
vector<int> dist;
vector<int> ans;

void bfs(int start){
  queue<int> q;
  q.push(start);
  dist[start] = 0;

  while (!q.empty()){
    int current = q.front();
    q.pop();

    for (int next : graph[current]){
      if (dist[next] == -1){
        dist[next] = dist[current] + 1;
        q.push(next);
      }
    }
  }
}

int main(){
  ios::sync_with_stdio(false);
  cin.tie(nullptr); cout.tie(nullptr);

  cin >> n >> m >> k >> x;
  graph.resize(n+1);
  dist.assign(n+1, -1);

  for (int i = 0; i<m; i++){
    int a, b;
    cin >> a >> b;
    graph[a].push_back(b);
  }

  bfs(x);

  for (int i = 1; i<=n; i++){
    if (dist[i] == k){
      ans.push_back(i);
    }
  }

  if (ans.empty()){
    cout << "-1";
  } else {
    sort(ans.begin(), ans.end());
    for (int city : ans){
      cout << city << "\n";
    }
  }

  return 0;
}