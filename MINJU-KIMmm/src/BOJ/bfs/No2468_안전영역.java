package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No2468_안전영역 {
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};

    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        arr=new int[N][N];
        int maxHeight=0;
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
                if(arr[i][j]>maxHeight){
                    maxHeight=arr[i][j];
                }
            }
        }

        //잠기는 높이 별로 브루트포스
        int maxArea=0;
        for(int h=0;h<maxHeight;h++){
            visited=new boolean[N][N];
            int cnt=0;
            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    //bfs 진행
                    if(!visited[i][j]&&arr[i][j]>h){
                        bfs(i,j,h);
                        cnt++;
                    }
                }
            }
            maxArea=Math.max(cnt, maxArea);
        }

        System.out.println(maxArea);
    }

    static void bfs(int x, int y, int h){
        Queue<Node> q=new LinkedList<>();
        q.offer(new Node(x,y));
        visited[x][y]=true;

        while(!q.isEmpty()){
            Node cur=q.poll();
            int px=cur.x;
            int py=cur.y;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=N)continue;

                if(!visited[nx][ny]&&arr[nx][ny]>h){
                    visited[nx][ny]=true;
                    q.add(new Node(nx,ny));
                }
            }
        }
    }

    static class Node{
        int x,y;

        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
