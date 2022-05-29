#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;

int binary_search(int left, int right, int target) {
    //재귀로 하면 너무 오래걸림 절대 안됨
    while(left <= right) {
        int mid = (left + right) / 2;
        if(arr[mid] == target) return 1;
        else if (arr[mid] > target) right = mid - 1;
        else left = mid + 1;
    }
    return 0;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, m, input;
    cin >> n;
    arr.assign(n, 0); //선언 후에 이렇게 초기화할 수 있구나
    for(int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());

    cin >> m;
    for(int i = 0; i < m; i++) {
        cin >> input;
        cout << binary_search(0, n-1, input) << "\n";
    }
}