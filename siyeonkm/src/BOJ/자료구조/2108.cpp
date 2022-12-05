#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <map>

using namespace std;

bool cmp(pair<int, int>& a, pair<int, int>& b) {
    return a.second > b.second;
}

int median(vector<int>& list, int size) {
    return list[size / 2];
}

int mode(vector<int>& list, int size) {
    int curr = 0;
    map<int, int> modeMap;
    vector<pair<int, int>> modeVec;
    for (int i = 0; i < size; i++) {
        if (modeMap.find(list[i]) != modeMap.end()) {
            auto itr = modeMap.find(list[i]);
            itr->second += 1;
        }
        else {
            modeMap.insert(make_pair(list[i], 1));
            curr++;
        }
    }
    for (auto& it : modeMap) {
        modeVec.push_back(it);
    }

    if (curr == 0) return modeVec[0].first; //1개일 경우를 이렇게 먼저 처리해야 sort할때 out of range 오류가 나지 않음

    sort(modeVec.begin(), modeVec.end(), cmp);
    if (modeVec[0].second == modeVec[1].second) {
        return modeVec[1].first;
    }
    else return modeVec[0].first;

}

int range(vector<int>& list, int size) {
    int min = list[0];
    int max = list[size - 1];
    return max - min;
}

int main() {
    int size;
    vector<int> list;
    vector<int> answer(4, 0);

    cin >> size;
    for (int i = 0; i < size; i++) {
        int num;
        cin >> num;
        list.push_back(num);

        answer[0] += num;
    }
    sort(list.begin(), list.end());
    answer[0] = floor((double)answer[0] / size + 0.5);
    answer[1] = median(list, size);
    answer[2] = mode(list, size);
    answer[3] = range(list, size);

    for (int i = 0; i < 4; i++) {
        cout << answer[i] << "\n";
    }
}