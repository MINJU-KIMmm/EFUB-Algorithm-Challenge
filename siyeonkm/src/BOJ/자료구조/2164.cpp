#include <iostream>
#include <queue>

using namespace std;

queue<int> createQueue(int num) {
    queue<int> card;
    for(int i=1; i<=num; i++) {
        card.push(i);
    }
    return card;
}

int solution(int num) {
    queue<int> card = createQueue(num);

    while(card.size()>1) {
        card.pop(); //맨 위 카드 삭제

        int front = card.front(); //그 다음으로 매위에 있는 카드를 밑으로
        card.pop();
        card.push(front);
    }
    return card.front();
}

int main() {
    int num;
    cin >> num;
    cout << solution(num);
}