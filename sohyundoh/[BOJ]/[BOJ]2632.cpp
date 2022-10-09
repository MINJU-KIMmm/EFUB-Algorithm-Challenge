#include <iostream>
#include <map>
#include <vector>
using namespace std;

// ��� ������ֱ� 
void make_matrix(vector<vector<int>>& _pizza_mat, vector<int>& _pizza_vec, int _size) {
    // ������ �� ��� ���� 
    for (int r_idx = 0; r_idx < _size; r_idx++) {
        for (int c_idx = r_idx; c_idx < _size; c_idx++) {
            // ����, �밢���� ��ġ�� �����̸� �ش� ������ ���� �־��ش�. 
            if (r_idx == c_idx) {
                _pizza_mat[r_idx][c_idx] = _pizza_vec[c_idx];
                continue;
            }
            // �ƴϸ� ���� ����� ������ + �迭������ ���� �߰��Ǿ�� �� �ε����� �� 
            _pizza_mat[r_idx][c_idx] = _pizza_mat[r_idx][c_idx - 1] + _pizza_vec[c_idx];
        }
    }
    // ���� �Ʒ� ��� ���� 
    for (int r_idx = 0; r_idx < _size; r_idx++)
        for (int c_idx = 0; c_idx < r_idx - 1; c_idx++)
            if (c_idx + 1 <= r_idx - 1)
                _pizza_mat[r_idx][c_idx] = _pizza_mat[0][_size - 1] - _pizza_mat[c_idx + 1][r_idx - 1];

}

// ���ڿ� ���� ������ ������ ����� ���� ���� ���� �� ������ ����.
// ex) �������� 7�� ���� ������ ��Ŀ��� �� ������ ���Ѵ�. 
void make_map(vector<vector<int>>& _pizza_mat, map<int, int>& _pizza_map, int _size) {
    for (int r_idx = 0; r_idx < _size; r_idx++) {
        for (int c_idx = 0; c_idx < _size; c_idx++) {
            int now_mat_val = _pizza_mat[r_idx][c_idx];
            // ���� ������?
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

    // ���� �� ��� ����� 
    // i �� j�� ���Ҵ� i~j ������ ���� �ǹ��Ѵ�. 
    vector<vector<int>> pizza_mat_a(M, vector<int>(M, 0));
    vector<vector<int>> pizza_mat_b(N, vector<int>(N, 0));

    make_matrix(pizza_mat_a, pizza_vec_a, M);
    make_matrix(pizza_mat_b, pizza_vec_b, N);

    // ����� Ž���ϸ鼭 �ش� ���� �ʿ� ���� 
    map<int, int> pizza_map_a;
    map<int, int> pizza_map_b;

    make_map(pizza_mat_a, pizza_map_a, M);
    make_map(pizza_mat_b, pizza_map_b, N);

    // ���ϰ��� �ϴ� ������ ũ�⸦ ���� ������ A�� B������ ũ�⸦ 
    // map ���� ã�Ƽ� �� �� �� 0�� �ƴ� ��쿡 ���信 �� ���� ���� �߰��Ѵ�. 
    int answer_num = 0;
    for (int a_size = 0; a_size <= want_size; a_size++) {
        int b_size = want_size - a_size;
        // �糡�� �ٸ��� ó�� 
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

        // �� ������ ���� �� �� �����ϸ� ���信 �߰� 
        if (pizza_map_a.find(a_size) != pizza_map_a.end() &&
            pizza_map_b.find(b_size) != pizza_map_b.end())
            answer_num += pizza_map_a[a_size] * pizza_map_b[b_size];
    }

    cout << answer_num;

    return 0;
}
Colored