#include <iostream>
#include <vector>

using namespace std;

long long solution(int room, vector<int> p, int main, int sub) {
    long long a = 0;
    for (int i = 0; i < room; i++) {
        int remain = p[i] - main;
        a++;
        if (remain > 0) {
            a += remain / sub;
            if (remain % sub != 0) a++;
        }
    }
    return a;
}

int main() {
    int room = 0;
    int main_d, sub_d = 0;
    long long answer = 0;

    cin>>room;
    vector<int> person(room);
    for (int i = 0; i < room; i++) {
        cin>>person[i];
    }
    cin>>main_d>>sub_d;

    answer = solution(room, person, main_d, sub_d);
    cout<<answer;
}