#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct cmp {
    bool operator()(const int& x1, const int& x2) const {
        int v1 = x1;
        int v2 = x2;
        if (x1 < 0) v1 = -x1;
        if (x2 < 0) v2 = -x2;
        
        if (v1 != v2) return v1 > v2;
        else if(v1 == v2) return x1 > x2; //절대값이 같으면 작은수로 출력
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int cnt, x;
    priority_queue<int, vector<int>, cmp> min_heap;
    //또는 찾아보니, 그냥 넣을때 음수를 달아주는것도 방법이라고 함

    cin >> cnt;
    for (int i = 0; i < cnt; i++) {
        cin >> x;
        if (x == 0) {
            if (!min_heap.empty()) {
                cout << min_heap.top() << "\n";
                min_heap.pop();
            }
            else {
                cout << "0" << "\n";
            }
        }
        else {
            min_heap.push(x);
        }
    }
}