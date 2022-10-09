#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int cnt_stick(string bracket) {
    int cnt = 0; // �踷��� ����
    vector<int> lazer; // ������ ��ġ ����

    stack<int> s; // ���� ��ȣ ��ġ ���� ����
    for (int i = 0; i < bracket.length(); i++) {
        if (bracket[i] == '(') s.push(i); // 1. ���� ��ȣ ������ push
        else if (bracket[i] == ')' && bracket[i - 1] == '(') { // 2. ������ �߰�
            lazer.push_back(i); s.pop(); // ������ ��ġ ���� �� ������ ���� ��ȣ ����
        }
        else if (bracket[i] == ')') { // 3. �踷��� ������ ���� �߰�
            int start_idx = s.top(); s.pop(); // (start_idx : ���� ����)

            int cut = 0; // (start_idx, i) ���� �ڸ��� ���� ����
            for (int j = 0; j < lazer.size(); j++) {
                if (lazer[j] > start_idx && lazer[j] < i) cut++;
            }
            cnt += (cut + 1); // �踷��� �� ����
        }
    }
    return cnt;
}

int main() {
    string bracket;
    cin >> bracket;

    cout << cnt_stick(bracket);
    return 0;
}