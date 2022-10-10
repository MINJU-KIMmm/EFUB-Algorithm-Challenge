#include <iostream>
#include <vector>

using namespace std;

pair<int, int> maxVisitor(int n, int x, vector<int> &visitor) {
    //윈도우 초기화
    int section_visitor = 0;
    for (int i = 0; i < x; i++)
        section_visitor += visitor[i];

    int max = section_visitor;
    int cnt = 1;

    //슬라이딩
    for (int i = x; i < n; i++) {
        section_visitor -= visitor[i - x];
        section_visitor += visitor[i];
        if (section_visitor > max) {
            cnt = 1;
            max = section_visitor;
        } else if (section_visitor == max)
            cnt++;
    }
    return make_pair(max, cnt);
}

int main() {
    int n, x;

    //입력
    cin >> n >> x;
    vector<int> visitor(n, 0);
    for (int i = 0; i < n; i++)
        cin >> visitor[i];

    //연산
    pair<int, int> max = maxVisitor(n, x, visitor);

    //출력
    if (ans.first == 0) {
        cout << "SAD\n";
        return 0;
    }
    cout << max.first << '\n' << max.second;
}