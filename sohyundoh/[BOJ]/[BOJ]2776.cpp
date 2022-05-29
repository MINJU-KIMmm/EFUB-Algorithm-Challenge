#include <iostream>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <set>

using namespace std;
int main(void)
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	int t;
	cin >> t;//테스트 케이스 개수 입력받기  

	for (int i = 0; i < t; i++) {
		int n;
		cin >> n;
        set<long long int>s;//s 선언(테스트케이스 만들 떄마다 초기화) 
		for (int j = 0; j < n; j++) {
			long long int temp;
			cin >> temp;
			s.insert(temp);
		}
		int m;
		cin >> m;
		for (int j = 0; j < m; j++) {
			long long int temp;
			cin >> temp;
			if (s.count(temp) == 1)cout << 1<<"\n";//원소가 s에 있는 개수가 1개이면 1 출력
			else cout << 0 << "\n";
		}
	}
	return 0;
}