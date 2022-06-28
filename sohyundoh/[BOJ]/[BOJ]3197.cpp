#include <iostream>
#include<queue>
#include<string>

using namespace std;

struct Que {
	int x;
	int y;
};

char board[1501][1501];
bool vis[1501][1501];

int dx[4] = { 0,1,0,-1 };
int dy[4] = { 1,0,-1,0 };

int main()
{
	int R, C;
	int lx, ly;
	string str;
	int time = 0;

	queue<Que> waterQ;
	cin >> R >> C;

	for (int i = 0; i < R; i++) {
		cin >> str;
		for (int j = 0; j < C; j++) {
			board[i][j] = str[j];
			if (board[i][j] == 'L') {
				lx = i;
				ly = j;//L��ġ
			}//���߿� �Էµ� L�� ��ġ�� ����ȴ�.
			if (board[i][j] == '.' or board[i][j] == 'L') {
				waterQ.push({ i,j });
			}
		}
	}

	queue<Que> Q;
	Q.push({ lx,ly });
	vis[lx][ly] = true;

	while (1) {
		queue<Que> nextQ;
		bool suc = false;
		while (!Q.empty() and !suc) {
			auto cur = Q.front();
			Q.pop();

			for (int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];

				if (nx<0 or nx>R - 1 or ny<0 or ny>C - 1)continue;

				if (board[nx][ny] == 'L' and vis[nx][ny] == false) {
					suc = true;
					break;
				}//�ٸ����� ������ ����
				if (board[nx][ny] == '.' and vis[nx][ny] == false) {
					Q.push({ nx,ny });
					vis[nx][ny] = true;
				}//���ε� �湮���������� ť�� �ִ´�.
				if (board[nx][ny] == 'X' and vis[nx][ny] == false) {
					nextQ.push({ nx,ny });
					vis[nx][ny] = true;
				}//������ �ִ� �����̸� ������ �湮�Ұ��̴�.
			}
		}
		if (suc) {
			cout << time << endl;
			break;
		}
		Q = nextQ;

		int watersize = waterQ.size();

		while (watersize--) {
			auto cur = waterQ.front();
			waterQ.pop();

			for (int i = 0; i < 4; i++) {
				int nx = cur.x + dx[i];
				int ny = cur.y + dy[i];
				if (nx<0 or nx>R - 1 or ny<0 or ny>C - 1)continue;
				if (board[nx][ny] == 'X') {
					waterQ.push({ nx,ny });
					board[nx][ny] = '.';
				}
			}
		}
		time++;

	}
}