#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

typedef pair<int, int> edge;
static vector<vector<edge>> A;
static vector<bool> visited;
static vector<int> m_distance;
void BFS(int node);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    int N;
    cin >> N;
    A.resize(N+1);

    for (int i = 0; i < N; i++){
        int S;
        cin >> S;
        while (true){
            int E, V;
            cin >> E;
            if (E==-1){
                break;
            }
            cin >> V;
            A[S].push_back(edge(E, V));
        }
    }

    m_distance = vector<int>(N+1, 0);
    visited=vector<bool>(N+1, false);
    BFS(1);
    int Max = 1;

    for (int i = 2; i <= N; i++){
        if (m_distance[Max] < m_distance[i]){
            Max=i;
        }
    }
    fill(m_distance.begin(), m_distance.end(), 0);
    fill(visited.begin(), visited.end(), false);
    BFS(Max);
    sort(m_distance.begin(), m_distance.end());
    cout << m_distance[N] << "\n";
}

void BFS(int index){
    queue<int> myqueue;
    myqueue.push(index);
    visited[index] = true;

    while (!myqueue.empty()) {
        int now_node = myqueue.front();
        myqueue.pop();
        for (edge i : A[now_node]) {
            if (!visited[i.first]){
                visited[i.first] = true;
                myqueue.push(i.first);
                m_distance[i.first] = m_distance[now_node]+i.second;
            }
        }
    }
}


// #include <iostream>
// #include <vector>
// #include <cstring>

// using namespace std;

// const int MAX = 100001;
// vector<pair<int, int>> tree[MAX];
// bool visited[MAX];
// int maxDist=0, farthestNode=0;

// void dfs(int node, int dist){
//     if (visited[node]) return;
//     visited[node] = true;

//     if (dist > maxDist){
//         maxDist = dist;
//         farthestNode = node;
//     }

//     for (auto &next: tree[node]){
//         int nextNode = next.first;
//         int nextDist = next.second;
//         dfs(nextNode, dist+nextDist);
//     }
// }

// int main(){
//     ios::sync_with_stdio(false);
//     cin.tie(nullptr); cout.tie(nullptr);

//     int V;
//     cin >> V;

//     for (int i = 0; i<V; i++){
//         int node;
//         cin >> node;

//         while (true){
//             int adj, cost;
//             cin >> adj;
//             if (adj==-1) break;
//             cin >> cost;
//             tree[node].push_back({adj, cost});
//             tree[adj].push_back({node, cost});
//         }
//     }

//     memset(visited, false, sizeof(visited));
//     dfs(1,0);

//     memset(visited, false, sizeof(visited));
//     maxDist=0;
//     dfs(farthestNode, 0);

//     cout << maxDist << "\n";
//     return 0;
// }