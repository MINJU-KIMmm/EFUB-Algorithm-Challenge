//
// Created by KangMinji on 2022-07-17.
//

#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<string, int> word_cnt;

/*
 * 길이가 m 이상인 단어들만 암기
 * 1) 자주 나오는 단어
 * 2) 단어 길이 길수록
 * 3) 알파벳 사전 순으로 앞에 있는 단어
 */
bool cmp(const string &a, const string &b) {
    if (word_cnt[a] != word_cnt[b])
        return word_cnt[a] > word_cnt[b];
    if (a.length() != b.length())
        return a.length() > b.length();
    return a < b;
}

int main() {
    int n, m;
    string word;
    vector<string> word_list;

    // 입력
    cin >> n >> m;
    while (n--) {
        cin >> word;

        if (word.length() < m)
            continue;
        if (!word_cnt[word])
            word_list.push_back(word);
        word_cnt[word]++;
    }

    // 연산
    sort(word_list.begin(), word_list.end(), cmp);

    // 출력
    for (int i=0; i<word_list.size(); i++)
        cout << word_list[i] << "\n";
}