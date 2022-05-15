#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> a;

int twoPointer(int size, int num) {
    int count = 0;
    int sum = a[0];
    int start = 0; int end = 0;
    while(end < size) {
        if(sum < num) {
            end++;
            if(end < size) sum+= a[end];
        }
        else if (sum > num) {
            sum -= a[start];
            start++;
        }
        else { //m이랑 같은 경우, start나 end중 하나만 옮기는 경우 반드시 m이 아니게 되므로 둘다 옮긴다.
            sum -= a[start];
            start++;
            end++;
            if(end < size) sum += a[end];
            count++;
        }
    }
    return count;
}

int main() {
    int n, m;
    cin >> n >> m;
    a.assign(n, 0);
    for(int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cout << twoPointer(n, m);
}