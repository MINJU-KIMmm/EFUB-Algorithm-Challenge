package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No16236_아기상어 {
    static int[][] arr;
    static int size=2;
    static int second=0;
    static int px=0;
    static int py=0;
    static int eat=0;

    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        arr=new int[N][N];
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
                if(arr[i][j]==9){
                    px=i;
                    py=j;
                    arr[i][j]=0;
                }
            }
        }

        while(true){
            PriorityQueue<Position> pq=new PriorityQueue<>((o1,o2)->
                    o1.d!=o2.d? Integer.compare(o1.d, o2.d):o1.x!=o2.x?Integer.compare(o1.x,o2.x):Integer.compare(o1.y,o2.y)
            );

            boolean[][] visited=new boolean[N][N];
            pq.add(new Position(px,py,0));
            visited[px][py]=true;

            boolean check=false;
            while(!pq.isEmpty()){
                Position cur=pq.poll();
                px=cur.x;
                py=cur.y;

                if(arr[px][py]!=0&&arr[px][py]!=0&&arr[px][py]<size){
                    arr[px][py]=0;
                    eat++;
                    second+=cur.d;
                    check=true;
                    break;
                }

                for(int i=0;i<4;i++){
                    int nx=cur.x+dx[i];
                    int ny=cur.y+dy[i];

                    if(nx<0||nx>=N||ny<0||ny>=N||visited[nx][ny]||arr[nx][ny]>size) continue;
                    pq.add(new Position(nx,ny,cur.d+1));
                    visited[nx][ny]=true;
                }
            }
            if(!check) break;
            if(size==eat){
                size++;
                eat=0;
            }
        }


        System.out.println(second);

    }



    static class Position {
        int x, y;
        int d;
        public Position(int x, int y, int d){
            this.x=x;
            this.y=y;
            this.d=d;
        }
    }
}
