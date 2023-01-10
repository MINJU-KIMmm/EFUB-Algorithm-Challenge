#include <string>
#include <vector>

using namespace std;

int cnt = 0;

void dfs(vector<int> &numbers, int target, int idx, int sum) {
    if(idx == numbers.size()) {
        if(sum == target) cnt++;
        return;
    }

    dfs(numbers, target, idx+1, sum+numbers[idx]);
    dfs(numbers, target, idx+1, sum-numbers[idx]);

    return;

}

int solution(vector<int> numbers, int target) {
    int answer = 0;

    dfs(numbers, target, 0, 0);
    answer = cnt;

    return answer;
}