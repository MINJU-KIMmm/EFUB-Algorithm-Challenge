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

	// �ڿ� Ȯ���ڸ� ���ܼ� ���Ϳ� ���
	for (int i = 0; i < N; i++)
	{
		cin >> s;
		s.erase(0, s.find('.') + 1);
		ex.push_back(s);

	}
	sort(ex.begin(), ex.end()); // ���������� ����

	tmp = ex[0]; 
	for (int i = 0; i < ex.size(); i++)
	{
		if (tmp == ex[i]) cnt++;  // ���� Ȯ���� ���� ����
		else if (tmp != ex[i]) // ���ο� Ȯ���ڵ���! 
		{
			re.push_back(pair<string, int>(tmp, cnt));
			// �����ϱ� 
			tmp = ex[i];
			cnt = 1;
		}
	}
	// Ȯ���ڸ��̶� ���� �ȴ��� ���� ���
	re.push_back(pair<string, int>(tmp, cnt));

	for (int i = 0; i < re.size(); i++)
	{
		cout << re[i].first << " " << re[i].second << endl;
	}
}
