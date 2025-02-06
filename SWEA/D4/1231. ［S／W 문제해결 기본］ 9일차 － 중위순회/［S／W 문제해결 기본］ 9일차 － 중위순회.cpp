#include <iostream>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

struct TreeNode {
    char value;
    int left, right;
};

void inOrderTraversal(int nodeIndex, const vector<TreeNode>& tree, string& result) {
    if (nodeIndex == -1) return;
    inOrderTraversal(tree[nodeIndex].left, tree, result);
    result += tree[nodeIndex].value;
    inOrderTraversal(tree[nodeIndex].right, tree, result);
}

int main() {
    int T=10;

    for (int test_case = 1; test_case <= T; ++test_case) {
        int N;
        cin >> N;
        cin.ignore();

        vector<TreeNode> tree(N + 1);
        for (int i = 1; i <= N; ++i) {
            string line;
            getline(cin, line);
            stringstream ss(line);

            int nodeNumber;
            char value;
            int left = -1, right = -1;
            ss >> nodeNumber >> value >> left >> right;

            tree[nodeNumber].value = value;
            tree[nodeNumber].left = left;
            tree[nodeNumber].right = right;
        }

        string result = "";
        inOrderTraversal(1, tree, result);
        cout << "#" << test_case << " " << result << endl;
    }

    return 0;
}
