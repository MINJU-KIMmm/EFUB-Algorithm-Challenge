#include <iostream>
using namespace std;
int R[10];
int result(void) {
	int n, x, y;
	int v[1000] = { 0, };//�ӷ� ������ �迭
	int fastest = 0;
	int flag = 0;
	int fastest_flag = 0;
	cin >> n >> x >> y; //�Է� �ޱ�
	for (int j = 0; j < n; j++) {
		cin >> v[j];
		if (v[j] > fastest) {
			fastest = v[j];//���� ���� �ӷ� ����
			fastest_flag = j;
		}
	}
	if (fastest == v[n - 1] && fastest_flag == n - 1) return 0;//�� �ӷ��� ���� ���� �ӷ��̶�� 0 ����
	float fastest_time = (float)x / (float)fastest; //���� ���� �ӷ����� �޸� ���� �ð� ���ϱ�
	for (int i = 0; i < y; i++) {
		if (fastest_time > ((float)(x - (i + 1)) / (float)v[n - 1]) + 1) return (i + 1); //���� �ν��ͷ� �� �Ÿ��� �����ϸ� ũ�� ���ϱ�.. ���� �������� ���� �� �� ����
		flag++;
	}
	if (flag == y - 1) return -1;//�������� ���ؼ� �ܵ� ����� �Ұ����ϴٸ� -1 ���
}
int main(void) {
	int t;
	cin >> t; //���̽����̽� ����
	for (int i = 0; i < t; i++) R[i] = result(); //�׽�Ʈ���̽� ��ŭ �Լ� ȣ�� �Լ� ���� �� ����
	for (int i = 0; i < t; i++) cout << R[i] << '\n'; //���� �� ���
}