//
// Created by KangMinji on 2022-07-24.
//

#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
using namespace std;

/*
 * 1) 1번 기술 -> 제일 위의 카드 바닥에 내려놓기 -> 제일 앞에 끼워넣기
 * 2) 2번 기술 -> 위에서 두 번째 카드 바닥에 내려놓기 -> 앞에서 두 번째에 끼워넣기
 * 3) 3번 기술 -> 제일 밑에 있는 카드 내려놓기 -> 제일 뒤에 끼워넣기
 * => 앞/뒤 끼워넣기가 있으므로 deque를 쓴다
 */
deque<int> cardGame(int n, vector<int> &card){
    deque<int> dq;

    for(int i=1; i<=n; i++){ //
        switch (card[i]) {
            case 1:
                dq.push_front(i);
                break;
            case 2:
            {
                int x = dq.front();
                dq.pop_front();
                dq.push_front(i);
                dq.push_front(x);
                break;
            }
            case 3:
                dq.push_back(i);
                break;
        }
    }
    return dq;
}

int main() {
    int n;
    cin >> n;

    // 입력
    vector<int> card(n+1, 0);
    for (int i=1; i<=n; i++) // i번째로 카드를 내려놓았을 때 card[i]번 기술을 쓴다 -> 1번째부터 시작하므로 i=1
        cin >> card[i];

    // 연산
    reverse(card.begin()+1, card.end()); // 거꾸로 생각하기 때문에 reverse 사용
    deque<int> dq = cardGame(n, card);

    // 출력
    while(!dq.empty()){
        cout << dq.front() << " ";
        dq.pop_front();
    }

}