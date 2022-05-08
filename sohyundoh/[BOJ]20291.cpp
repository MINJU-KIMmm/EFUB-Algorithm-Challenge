#include<iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;

int N, cnt = 0;
vector<pair<string, int>> re;
vector<string> ex; // extension
string s, tmp;

int main()
{
	cin >> N;

	// 뒤에 확장자만 남겨서 벡터에 담기
	for (int i = 0; i < N; i++)
	{
		cin >> s;
		s.erase(0, s.find('.') + 1);
		ex.push_back(s);

	}
	sort(ex.begin(), ex.end()); // 사전순으로 정렬

	tmp = ex[0]; 
	for (int i = 0; i < ex.size(); i++)
	{
		if (tmp == ex[i]) cnt++;  // 같은 확장자 개수 세기
		else if (tmp != ex[i]) // 새로운 확장자등장! 
		{
			re.push_back(pair<string, int>(tmp, cnt));
			// 리셋하기 
			tmp = ex[i];
			cnt = 1;
		}
	}
	// 확장자명이랑 개수 안담긴거 마저 담기
	re.push_back(pair<string, int>(tmp, cnt));

	for (int i = 0; i < re.size(); i++)
	{
		cout << re[i].first << " " << re[i].second << endl;
	}
}
