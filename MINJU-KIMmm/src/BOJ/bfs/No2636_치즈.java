package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No2636_치즈 {
    static int[][] arr;
    static int H, W;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static boolean[][] visited;
    static int time=0;
    static int remain=0;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        H=Integer.parseInt(st.nextToken());
        W= Integer.parseInt(st.nextToken());
        arr=new int[H][W];
        visited=new boolean[H][W];

        for(int i=0;i<H;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<W;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        int firstCheese=calcCount();
        int count=0;
        while(true){
            time++;
            bfs(0,0);
            visited=new boolean[H][W]; // visited 초기화

            remain=count;
            count=calcCount(); //치즈개수 계산
            if(count==0) break; //다 녹이면 break
        }

        System.out.println(time);
        System.out.println(time==1? firstCheese:remain);
    }

    static void bfs(int x, int y){
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

                if(nx<0||nx>=H||ny<0||ny>=W||visited[nx][ny]) continue;

                if(arr[nx][ny]==1){
                    arr[nx][ny]=2;
                    visited[nx][ny]=true;
                }
                if(arr[nx][ny]==0){
                    q.offer(new Node(nx,ny));
                    visited[nx][ny]=true;
                }
            }
        }

        // 치즈 녹이기
        for(int i=0;i<H;i++){
            for(int j=0;j<W;j++){
                if(arr[i][j]==2) arr[i][j]=0;
            }
        }
    }

    //개수 계산
    static int calcCount(){
        int count=0;

        for(int i=0;i<H;i++){
            for(int j=0;j<W;j++){
                if(arr[i][j]==1) count++;
            }
        }

        return count;
    }

    static class Node {
        int x, y;
        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}



