#include <string>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    sort(begin(lost), end(lost));
    sort(begin(reserve), end(reserve));
    for (int j = 0; j < lost.size(); j++){
        if (find(reserve.begin(), reserve.end(), lost[j]) != reserve.end()) {
            reserve.erase(remove(reserve.begin(), reserve.end(), lost[j]), reserve.end());
            lost.erase(remove(lost.begin(), lost.end(), lost[j]), lost.end());
        }
    }
    answer = n - lost.size();
    for (int i = 0; i < lost.size(); i++) {
        if (find(reserve.begin(), reserve.end(), lost[i] - 1) != reserve.end()) {
            reserve.erase(remove(reserve.begin(), reserve.end(), lost[i] - 1), reserve.end());
            answer++;
        }
        else if (find(reserve.begin(), reserve.end(), lost[i] + 1) != reserve.end()) {
            reserve.erase(remove(reserve.begin(), reserve.end(), lost[i] + 1), reserve.end());
            answer++;
        }else if (find(reserve.begin(), reserve.end(), lost[i]) != reserve.end()) {
            reserve.erase(remove(reserve.begin(), reserve.end(), lost[i]), reserve.end());
            answer++;
        }
    }
    return answer;
}

int main() {
    int n;
    cin >> n;
    string lost_arr;
    string reserve_arr;
    vector<int> lost;
    vector<int> reserve;
    cin >> lost_arr;
    cin >> reserve_arr;
    for (int i = 1; i < lost_arr.length() - 1; i++) {
        if (lost_arr[i] != ' ' && lost_arr[i] != ',') {
            lost.push_back(lost_arr[i]);
        }
    }
    for (int k = 1; k < reserve_arr.length() - 1; k++) {
        if (reserve_arr[k] != ' ' && reserve_arr[k] != ',') {
            reserve.push_back(reserve_arr[k]);
        }
    }
    cout << solution(n, lost, reserve);
    return 0;
}