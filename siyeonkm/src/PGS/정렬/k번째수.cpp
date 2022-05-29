#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;

    for (int i = 0; i < commands.size(); i++){
        int first = commands[i][0] - 1;
        int last = commands[i][1];
        int key = commands[i][2] - 1;
        vector<int> temp;

        for (int j = first; j < last; j++)
            temp.push_back(array[j]);
        sort(temp.begin(), temp.end());
        answer.push_back(temp.at(key));
    }

    return answer;
}