#include <iostream>
#include <vector>

using namespace std;
vector<int> uf;
//처음엔 원소 하나하나가 집합임
//0 - 같은 집합으로 합침
//1 - 같은집합인지 확인

int find(int node) {
    if (uf[node] < 0) {
        return node;
    }
    return uf[node] = find(uf[node]);
}

void merge(int a, int b) {
    int parentA, parentB;
    parentA = find(a);
    parentB = find(b);
    if(parentA == parentB) return;

    if (uf[parentA] < uf[parentB]) { //a쪽 집합이 더 큼. 그러니까 b가 속한 집합을 a부모쪽에 달아주기
        uf[parentB] = parentA;
        uf[parentA] = uf[parentA] - 1;
    }
    else if (uf[parentA] > uf[parentB]) { //반대
        uf[parentA] = parentB;
        uf[parentB] = uf[parentB] - 1;
    }
    else if (uf[parentA] == uf[parentB]) {
        uf[parentB] = parentA;
        uf[parentA] = uf[parentA] - 1;
    }
    return;
}

int main() {
    cin.tie(0);
	cin.sync_with_stdio(false);

    int n, m;
    cin >> n >> m;
    uf.assign(n+1, -1);

    for (int i = 0; i < m; i++) {
        int operation, a, b;
        cin >> operation >> a >> b;

        if (operation == 1) {
            if (find(a) == find(b)) cout << "YES" << '\n';
            else cout << "NO" << '\n';
        }
        else {
            merge(a, b);
        }
    }
    return 0;
}