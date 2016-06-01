#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    double meal;
    int tip, tax;
    cin >> meal;
    cin >> tip;
    cin >> tax;
    double calculation = meal + (meal * tip + meal * tax) / 100;
    int totalCost = calculation;
    cout << "The total meal cost is " << totalCost << " dollars.";
    return 0;
}