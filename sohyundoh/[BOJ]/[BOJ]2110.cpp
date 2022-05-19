#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
long long x[200000];
void cal(long long x[], int n, int c) {
	vector<long long> v;
	for (int j = 0; j < n; j++) {
		v.push_back(x[j]);
	}
	sort(v.begin(), v.end()); //입력받은 배열을 순서 대로 나열
	long long start = 1, end = v[n - 1] - v[0]; //1과 , 거리가 가장 큰 차이가 나는 값을 저장.
	int temp = 0;//공유기 간의 거리 세어주는 변수
	while (start <= end) {
		long long home = v[0]; //제일 작은 좌표를 가진 집 변수에 저장
		long long mid = (start + end) / 2; //1과 거리가 가장 긴 것을 더한 것의 절반을 구함
		int cnt = 1;//공유기의 개수를 세어주는 변수
		for (int k = 0; k < n; ++k) {
			if (v[k] - home >= mid) {//가장 작은 좌표를 가진 집에서의 거리가 mid 보다 크다면 
				++cnt;//cnt를 키워줌
				home = v[k];//그리고 home 바꾸기 
			}
			if (cnt >= c) { //cnt 값이 공유기 개수보다 많거나 같다면
				temp = mid;//공유기 간의 거리에 mid를 저장
				start = mid + 1;//간격 높이기
			}
			else {
				end = mid - 1;//간격 낮추기
			}
		}
	}
	cout << temp;
}
int main(void) {
	int n, c;
	cin >> n >> c;
	for (int i = 0; i < n; i++) {
		cin >> x[i];
	}
	cal(x, n, c);
}
