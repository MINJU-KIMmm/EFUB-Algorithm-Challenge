#include <iostream>
#include <vector>
#include <set>
#include <algorithm>
#include <queue>

using namespace std;


int n, m, r;
vector<int> item;
vector<pair<int, int>> connect[101];

int answer = 0;
int dijkstra(int start, int end) {
    //cout << 'h';

    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
    pq.push({0, start});
    vector<int> dis_list(n+1, (int)1e9);
    dis_list[start] = 0;
    
    int take = 0;
//    bool visited[n+1];
    while(!pq.empty()) {
        auto now = pq.top();
        pq.pop();
        
        //cout << now.first << ' ' << now.second << '\n';
        
        if(now.first > dis_list[now.second]) continue;
        
        for(auto next:connect[now.second]) {
//            cout << 'n' <<  next.second << ' ';
            if(next.first+now.first < dis_list[next.second]) {
                dis_list[next.second] = next.first+now.first;
                pq.push({dis_list[next.second], next.second});
            }
        }
    }
//    cout << end << ' ' << item[end] << ' ' << dis_list[end] << endl;
    if(dis_list[end]<=m) return item[end];
    else return 0;
}

int main() {
    cin >> n;
    cin >> m;
    cin >> r;
    
    item.push_back(0);
    for(int i=0;i<n;i++) {
        int num; cin >> num;
        item.push_back(num);
    }
    
    for(int i=0;i<r;i++) {
        int a; cin >> a;
        int b; cin >> b;
        int l; cin >> l;
        
        connect[a].push_back({l, b});
        connect[b].push_back({l, a});
    }
    
    for(int i=1;i<=n;i++) {
        int here = 0;
        for(int j=1;j<=n;j++) {
            here += dijkstra(i, j);
//            cout << here << endl;
        }
        answer = max(answer, here);
    }
    
    cout << answer;
}
