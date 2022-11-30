#include <iostream>
#include <queue>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    int num, i, x;
    priority_queue<int> heap;
    
    cin >> num;
    for(i=0; i<num; i++) {
        cin >> x;
        
        if(x == 0) {
            if(!heap.empty()) {
                cout << heap.top() << "\n";
                heap.pop();
            }else cout << 0 << "\n";
        }
        else heap.push(x);
    }
}