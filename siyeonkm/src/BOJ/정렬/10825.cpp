#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

struct student {
    string name;
    int korean, english, math;
};

bool compare(const student &s1, const student &s2) {
    if (s1.korean != s2.korean) //국어 점수가 다르다면 감소하는 순서
        return s1.korean > s2.korean;
    else if (s1.english != s2.english) //영어 점수가 다르다면 증가하는 순서
        return s1.english < s2.english;
    else if (s1.math != s2.math) //수학 점수가 다르다면 감소하는 순서
        return s1.math > s2.math;
    else return s1.name < s2.name; //이름이 사전 순으로 증가하는 순서
}

int main() {
    int num, i;

    cin >> num;
    vector<student> students(num);

    for(i=0; i<num; i++) {
        cin>>students[i].name>>students[i].korean>>students[i].english>>students[i].math;
    }

    sort(students.begin(), students.end(), compare);

     for (int i = 0; i < num; i++) {
         cout << students[i].name << '\n';
     }

}