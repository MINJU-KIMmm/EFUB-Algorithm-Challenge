#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct student {
    string name;
    int kor, eng, math;
};


bool compare(const student &a, const student &b) {
    //국영수이름 순으로 비교
    if (a.kor != b.kor) {
        return a.kor > b.kor;
    }
    if (a.eng != b.eng) {
        return a.eng < b.eng;
    }
    if (a.math != b.math) {
        return a.math > b.math;
    }
    return a.name < b.name;
}

int main() {
    int n;
    cin >> n;

    vector<student> school(n);

    for (int i = 0; i < n; i++) {
        cin >> aschool[i].name >> school[i].kor >> school[i].eng >> school[i].math;
    }
    sort(school.begin(), school.end(), compare);

    for (int i = 0; i < n; i++) {
        cout << school[i].name << '\n';
    }
    return 0;
}