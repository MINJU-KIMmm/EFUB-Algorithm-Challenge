//
// Created by KangMinji on 2022-07-02.
//

#include <iostream>
#include <cmath>
using namespace std;
typedef pair<int, int> ci;

ci diet(int D, int W0, int I, int I0, int T, int A){
    while(D--){
        int O = I0 + A; // 일일 에너지 소비량
        W0 += (I - O); // 체중

        if (abs(I-O) > T)
            I0 += floor((double)(I - O)/2);

        if (W0 <= 0 || I0 <= 0)
            return ci(0, 0);
    }
    return ci(W0, I0);
}

int main(){

    /*
     * 체중 : 일일 에너지 섭취량(I) - 일일 에너지 소비량(O) (일일 기초 대사량(I0) + 일일 활동 대사량(A)
     * IF |일일 에너지 섭취량(I) - 일일 에너지 소비량(O)| > T
     * -> 일일 기초 대사량(B) += floor(일일 에너지 섭취량(I) - 일일 에너지 소비량(O)/2)
     *
     * 사망 조건 : 체중(W) <= 0 || 일일 기초 대사량(I0) <= 0
     */

    int W0, I0, T, D, I, A;
    cin >> W0 >> I0 >> T; // 다이어트 전 체중(W0), 일일 에너지 섭취량(I0), 일일 기초 대사량(I0), 기초대사량 역치(T)
    cin >> D >> I >> A; // 다이어트 기간(D), 일일 에너지 섭취량(I), 일일 활동 대사량(A)

    // 1) 일일 기초 대사량의 변화 고려 X
    int W = W0 + (I - (I0 + A)) * D;
    if (W <= 0)
        cout << "Danger Diet\n";
    else
        cout << W << " " << I0 << "\n";

    // 2) 일일 기초 대사량의 변화 고려 O
    ci result = diet(D, W0, I, I0, T, A);
    if (result.first <= 0 || result.second <= 0)
        cout << "Danger Diet";

    // 3) 요요 여부
    else {
        string ans = "NO";
        // 변화한 일일 대사량을 가지고 다이어트 전 일일 에너지 섭취량(I0)과 활동 대사량(0)으로 돌아갈 경우
        if (I0 - result.second > 0)
            ans = "YOYO";
        cout << result.first << " " << result.second << " " << ans << "\n";
    }
}