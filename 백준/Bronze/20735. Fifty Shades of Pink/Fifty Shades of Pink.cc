#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main() {
    int N;
    cin >> N;
    cin.ignore();

    vector<string> packages(N);
    for (int i = 0; i < N; ++i) {
        getline(cin, packages[i]);
        transform(packages[i].begin(), packages[i].end(), packages[i].begin(), ::tolower);
    }

    int count = 0;
    for (const string& package : packages) {
        if (package.find("pink") != string::npos || package.find("rose") != string::npos) {
            count++;
        }
    }

    if (count > 0) {
        cout << count << endl;
    } else {
        cout << "I must watch Star Wars with my daughter" << endl;
    }

    return 0;
}
