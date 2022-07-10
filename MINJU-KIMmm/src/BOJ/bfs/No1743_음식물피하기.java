package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No1743_음식물피하기 {

    static int N, M, K;
    static int[][] arr;
    static boolean[][] visited;
    static int area=0, answer=0;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());
        K=Integer.parseInt(st.nextToken());

        arr=new int[N][M];
        visited=new boolean[N][M];
        for(int i=0;i<K;i++){
            st=new StringTokenizer(br.readLine());
            int r=Integer.parseInt(st.nextToken());
            int c=Integer.parseInt(st.nextToken());

            arr[r-1][c-1]=1;
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(!visited[i][j]&&arr[i][j]==1){
                    bfs(i,j);
                    answer=Math.max(area,answer);
                }
            }
        }

        System.out.println(answer);
    }

    static int[]dx={-1,1,0,0};
    static int[]dy={0,0,-1,1};
    static void bfs(int x, int y){
        area=1;
        Queue<Node> q=new LinkedList<>();

        visited[x][y]=true;
        q.add(new Node(x,y));

        while(!q.isEmpty()){
            Node cur=q.poll();
            int px=cur.x;
            int py=cur.y;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=M||visited[nx][ny] ) continue;

                if(arr[nx][ny]==1){
                    area++;
                    q.add(new Node(nx,ny));
                    visited[nx][ny]=true;
                }
            }
        }
    }

    static class Node{
        int x, y;
        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
