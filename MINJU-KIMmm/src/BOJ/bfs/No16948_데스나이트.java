package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No16948_데스나이트 {
    static int[] dx={-2,-2,0,0,2,2};
    static int[] dy={-1,1,-2,2,-1,1};
    static boolean[][] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        int r1=Integer.parseInt(st.nextToken());
        int c1=Integer.parseInt(st.nextToken());
        int r2=Integer.parseInt(st.nextToken());
        int c2=Integer.parseInt(st.nextToken());


        visited=new boolean[N][N];
        boolean flag=false;

        Queue<Node> q=new LinkedList<>();
        q.offer(new Node(r1,c1,0));
        visited[r1][c1]=true;

        int cnt=0;
        l: while(!q.isEmpty()){
            Node cur=q.poll();
            int x=cur.x;
            int y=cur.y;

            for(int i=0;i<6;i++){
                int nx=x+dx[i];
                int ny=y+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=N||visited[nx][ny]) continue;
                if(nx==r2&&ny==c2){
                    flag=true;
                    cnt=cur.cnt+1;
                    break l;
                }
                visited[nx][ny]=true;
                q.offer(new Node(nx,ny,cur.cnt+1));
            }
        }

        System.out.println(flag? cnt:-1);
    }

    static class Node {
        int x, y, cnt;
        public Node(int x, int y, int cnt){
            this.x=x;
            this.y=y;
            this.cnt=cnt;
        }
    }
}
