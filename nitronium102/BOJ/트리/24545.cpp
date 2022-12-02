//
// Created by KangMinji on 2022-11-22.
//

#include <iostream>
#include <vector>
using namespace std;

// 정점 숫자 연속 -> 벡터 / 인접 리스트 형태
vector<vector<int>> tree;

/*
 * 1) 4개 이상의 정점과 인접한 정점은 없다
 * 2) 인접한 정점의 개수가 3개인 정점 : 1개만 존재
 * 3) 인접한 정점이 하나뿐인 정점 : 3개만 존재
 * => 어떤 노드를 살려야 할까?
 * 중심이 되는 노드 1개 + 해당 노드에 연결된 간선 3개
 * => 한 방향으로 연결된 노드 개수가 가장 많은 간선 3개를 가진 노드
 */
int main() {
    int n, u, v;

    // 입력
    cin >> n;

    // 초기화
    tree.assign(n, vector<int>(0));
    while(n--){
        cin >> u >> v;
        tree[u].push_back(v);
        tree[v].push_back(u);
    }
}