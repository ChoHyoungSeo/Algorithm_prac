#include <iostream>
using namespace std;
int main() {
    int weight, bmi;
    double height;
    cin >> height >> weight;
    height = height / 100;
    bmi = weight / (height*height);
    cout << bmi << endl;
    
    if (bmi > 25){
        cout << "Obesity";
    }

    return 0;
}