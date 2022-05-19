#include <iostream>
using namespace std;
int R[10];
int result(void) {
	int n, x, y;
	int v[1000] = { 0, };//속력 저장할 배열
	int fastest = 0;
	int flag = 0;
	int fastest_flag = 0;
	cin >> n >> x >> y; //입력 받기
	for (int j = 0; j < n; j++) {
		cin >> v[j];
		if (v[j] > fastest) {
			fastest = v[j];//가장 빠른 속력 저장
			fastest_flag = j;
		}
	}
	if (fastest == v[n - 1] && fastest_flag == n - 1) return 0;//내 속력이 가장 빠른 속력이라면 0 리턴
	float fastest_time = (float)x / (float)fastest; //가장 빠른 속력으로 달릴 때의 시간 구하기
	for (int i = 0; i < y; i++) {
		if (fastest_time > ((float)(x - (i + 1)) / (float)v[n - 1]) + 1) return (i + 1); //내가 부스터로 갈 거리를 조정하며 크기 비교하기.. 만일 빨라지는 순간 그 값 리턴
		flag++;
	}
	if (flag == y - 1) return -1;//빨라지지 못해서 단독 우승이 불가능하다면 -1 출력
}
int main(void) {
	int t;
	cin >> t; //테이스케이스 개수
	for (int i = 0; i < t; i++) R[i] = result(); //테스트케이스 만큼 함수 호출 함수 리턴 값 저장
	for (int i = 0; i < t; i++) cout << R[i] << '\n'; //리턴 값 출력
}