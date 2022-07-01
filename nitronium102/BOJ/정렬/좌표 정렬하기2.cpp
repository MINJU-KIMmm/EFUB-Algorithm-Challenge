//
// Created by KangMinji on 2022-07-01.
//

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
typedef pair<int, int> ci;

bool comp(const ci &a, const ci &b){
    if (a.second != b.second)
        return a.second < b.second;
    return a.first < b.first;
}

int main(){
    int n;
    vector<ci> grid;

    // 입력
    cin >> n;
    grid.assign(n, {0, 0});
    for (int i=0; i<n; i++)
        cin >> grid[i].first >> grid[i].second;

    // 연산
    sort(grid.begin(), grid.end(), comp);

    // 출력
    for (int i=0; i<n; i++)
        cout << grid[i].first << " " << grid[i].second << "\n";
}