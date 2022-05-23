#include <iostream>
#include <vector>

using namespace std;

typedef pair<int, int> ci;
vector<int> path;

ci lis(int size, vector<int>& list) {
    vector<int> dp(size, 1);
    ci ans = {1, 0};

    for (int i = 1; i < size; i++) {
        int index = -1;
        for(int j = 0; j < i; j++) {
            if(list[i] > list[j] && dp[i] < dp[j] + 1) {
                dp[i] = dp[j] + 1;
                index = j;
            }
        }
        path[i] = index;
        if(ans.first < dp[i]) ans = {dp[i], i};
    }
    return ans;
}

int main() {
    int size;
    cin >> size;
    vector<int> list(size);
    path.assign(size, -1);

    for (int i = 0; i < size; i++) {
        cin >> list[i];
    }
    ci ans = lis(size, list);
    int index  = ans.second;
    cout << ans.first << "\n";

    vector<int> answer;

    while (index != -1) {
        answer.push_back(list[index]);
        index = path[index];
    }

    for (int i = answer.size() - 1; i >= 0; i--) {
        cout << answer[i] << " ";
    }
    return 0;
}