#include <iostream>
#include <set>
using namespace std;

int main() {
    string s;
    cin >> s; 

    set<string> arr; 

    string str = "";
    for (int i = 0; i < s.size(); i++) {
        for (int j = i; j < s.size(); j++) {
            str += s[j];
            arr.insert(str);
        }
        str = "";
    }

    cout << arr.size();
}
