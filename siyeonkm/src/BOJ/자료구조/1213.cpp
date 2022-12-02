#include <string>
#include <iostream>
#include <vector>

using namespace std;

vector<int> countAlpha(string input) {
    vector<int> count(26, 0);
    for(int i=0; i<input.size(); i++) {
        count[input[i]-'A']++;
    }
    return count;
}

string makePalindrome(vector<int> &count) {
    string part1 = "", part2 = "", part3 = "";

    for (int i = 0; i < 26; i++) {
        if (count[i] % 2 == 1) {
            if (part2.size() == 1) {
                return "I'm Sorry Hansoo";
            }
            part2 = (char) (i + 'A');
        }

        for (int j = 0; j < count[i] / 2; j++) {
            part1 += (char) (i + 'A');
            part3 = (char) (i + 'A') + part3; //뒤에서부터 입력하려고 이렇게 구현
        }
    }

    return part1 + part2 + part3;
}

int main() {
    string input;
    cin >> input;

    vector<int> count = countAlpha(input);
    cout << makePalindrome(count);
}