#include <iostream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

vector<string> split(string input, char delimiter);
int mySum(string a);

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int ans = 0;
    string example;
    cin >> example;
    vector<string> str = split(example, '-');

    for (int i = 0; i<str.size(); i++){
        int tmp = mySum(str[i]);
        if (i==0){
            ans += tmp;
        }
        else{
            ans -= tmp;
        }
    }
    cout << ans << "\n";
}

vector<string> split(string input, char delimiter){
    vector<string> result;
    stringstream ss(input);
    string splitdata;

    while (getline(ss, splitdata, delimiter)){
        result.push_back(splitdata);
    }
    return result;
}

int mySum(string a){
    int sum = 0;
    vector<string> tmp = split(a, '+');
    
    for (int i = 0; i<tmp.size(); i++){
        sum += stoi(tmp[i]);
    }

    return sum;
}