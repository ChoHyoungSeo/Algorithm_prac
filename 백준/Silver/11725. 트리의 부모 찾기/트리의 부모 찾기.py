import sys
from collections import deque
input = sys.stdin.readline

def find_tree_parents():
    n = int(input().strip())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().strip().split())
        tree[a].append(b)
        tree[b].append(a)

    parents = [0] * (n + 1)
    queue = deque([1])
    parents[1] = -1

    while queue:
        current_node = queue.popleft()
        for next_node in tree[current_node]:
            if parents[next_node] == 0:
                parents[next_node] = current_node
                queue.append(next_node)

    for i in range(2, n + 1):
        print(parents[i])

if __name__ == "__main__":
    find_tree_parents()
