//
// Created by KangMinji on 2022-05-04.
//

#include <iostream>
using namespace std;

bool check(int i, int j, int k){
    // i는 23까지라 몫에서 3 나올 확률 X
    if (i%10 == 3 || j%10 == 3 || j/10 == 3 || k%10 == 3 || k/10 == 3)
        return true;
    return false;
}

int main(){
    int N;
    int cnt = 0;

    cin >> N;
    for (int i=0; i<=N; i++){
        for (int j=0; j<60; j++){
            for (int k=0; k<60; k++){
                if (check(i, j, k))
                    cnt++;
            }
        }
    }
    cout << cnt << "\n";
}