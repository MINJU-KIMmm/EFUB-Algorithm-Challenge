#include <iostream>
#include <map>
#include <vector>
using namespace std;

// 행렬 만들어주기 
void make_matrix(vector<vector<int>>& _pizza_mat, vector<int>& _pizza_vec, int _size) {
    // 오른쪽 위 행렬 갱신 
    for (int r_idx = 0; r_idx < _size; r_idx++) {
        for (int c_idx = r_idx; c_idx < _size; c_idx++) {
            // 만약, 대각선에 위치한 원소이면 해당 원소의 값을 넣어준다. 
            if (r_idx == c_idx) {
                _pizza_mat[r_idx][c_idx] = _pizza_vec[c_idx];
                continue;
            }
            // 아니면 이전 행렬의 값에서 + 배열에서의 현재 추가되어야 할 인덱스의 값 
            _pizza_mat[r_idx][c_idx] = _pizza_mat[r_idx][c_idx - 1] + _pizza_vec[c_idx];
        }
    }
    // 왼쪽 아래 행렬 갱신 
    for (int r_idx = 0; r_idx < _size; r_idx++)
        for (int c_idx = 0; c_idx < r_idx - 1; c_idx++)
            if (c_idx + 1 <= r_idx - 1)
                _pizza_mat[r_idx][c_idx] = _pizza_mat[0][_size - 1] - _pizza_mat[c_idx + 1][r_idx - 1];

}

// 피자에 구간 합으로 가능한 경우의 수를 값에 따라서 몇 개인지 센다.
// ex) 구간합이 7인 것의 개수가 행렬에서 몇 개인지 구한다. 
void make_map(vector<vector<int>>& _pizza_mat, map<int, int>& _pizza_map, int _size) {
    for (int r_idx = 0; r_idx < _size; r_idx++) {
        for (int c_idx = 0; c_idx < _size; c_idx++) {
            int now_mat_val = _pizza_mat[r_idx][c_idx];
            // 값이 없으면?
            if (_pizza_map.find(now_mat_val) == _pizza_map.end())
                _pizza_map[now_mat_val] = 1;
            else
                _pizza_map[now_mat_val]++;
        }
    }
}

int main() {
    int want_size, M, N;
    cin >> want_size >> M >> N;
    vector<int> pizza_vec_a(M);
    vector<int> pizza_vec_b(N);

    // input 
    for (int m_idx = 0; m_idx < M; m_idx++)
        cin >> pizza_vec_a.at(m_idx);
    for (int n_idx = 0; n_idx < N; n_idx++)
        cin >> pizza_vec_b.at(n_idx);

    // 구간 합 행렬 만들기 
    // i 행 j열 원소는 i~j 까지의 합을 의미한다. 
    vector<vector<int>> pizza_mat_a(M, vector<int>(M, 0));
    vector<vector<int>> pizza_mat_b(N, vector<int>(N, 0));

    make_matrix(pizza_mat_a, pizza_vec_a, M);
    make_matrix(pizza_mat_b, pizza_vec_b, N);

    // 행렬을 탐색하면서 해당 값을 맵에 저장 
    map<int, int> pizza_map_a;
    map<int, int> pizza_map_b;

    make_map(pizza_mat_a, pizza_map_a, M);
    make_map(pizza_mat_b, pizza_map_b, N);

    // 원하고자 하는 피자의 크기를 토대로 가능한 A와 B에서의 크기를 
    // map 에서 찾아서 두 개 다 0이 아닌 경우에 정답에 두 수의 곱을 추가한다. 
    int answer_num = 0;
    for (int a_size = 0; a_size <= want_size; a_size++) {
        int b_size = want_size - a_size;
        // 양끝점 다르게 처리 
        if (a_size == 0) {
            if (pizza_map_b.find(b_size) != pizza_map_b.end())
                answer_num += pizza_map_b[b_size];
            continue;
        }
        if (b_size == 0) {
            if (pizza_map_a.find(a_size) != pizza_map_a.end())
                answer_num += pizza_map_a[a_size];
            continue;
        }

        // 두 피자의 값이 둘 다 존재하면 정답에 추가 
        if (pizza_map_a.find(a_size) != pizza_map_a.end() &&
            pizza_map_b.find(b_size) != pizza_map_b.end())
            answer_num += pizza_map_a[a_size] * pizza_map_b[b_size];
    }

    cout << answer_num;

    return 0;
}
Colored