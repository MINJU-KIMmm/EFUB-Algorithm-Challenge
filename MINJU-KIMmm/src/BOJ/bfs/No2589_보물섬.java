package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No2589_보물섬 {
    static int N,M;
    static char[][] arr;
    static int[][] cost;
    static boolean[][] visited;
    static int answer=Integer.MIN_VALUE;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        arr=new char[N][M];
        cost=new int[N][M];
        visited=new boolean[N][M];

        for(int i=0;i<N;i++){
            String str=br.readLine();
            for(int j=0;j<M;j++){
                arr[i][j]=str.charAt(j);
            }
        }

        for(int i=0;i<N;i++){
            for(int j=0;j<M;j++){
                if(arr[i][j]=='L'){
                    visited=new boolean[N][M];
                    cost=new int[N][M];
                    int now=bfs(i,j);
                    answer=Math.max(now, answer);
                }
            }
        }

        System.out.println(answer);
    }

    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};

    static int bfs(int x, int y){
        Queue<Node>q=new LinkedList<>();
        q.offer(new Node(x,y));
        visited[x][y]=true;

        int max=0;

        cost[x][y]=0;

        while(!q.isEmpty()){
            Node cur=q.poll();
            int px=cur.x;
            int py=cur.y;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=M||visited[nx][ny]) continue;

                if(arr[nx][ny]=='L'){
                    q.offer(new Node(nx,ny));
                    visited[nx][ny]=true;
                    cost[nx][ny]=cost[px][py]+1;
                    max=Math.max(max, cost[nx][ny]);
                }
            }
        }

        return max;
    }

    static class Node{
        int x,y;
        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
