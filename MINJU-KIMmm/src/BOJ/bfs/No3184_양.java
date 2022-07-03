package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No3184_양 {
    static char[][] arr;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static int sheep=0;
    static int wolf=0;

    static int R,C;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        R=Integer.parseInt(st.nextToken());
        C=Integer.parseInt(st.nextToken());

        arr=new char[R][C];
        visited=new boolean[R][C];
        for(int i=0;i<R;i++){
            String str=br.readLine();
            for(int j=0;j<C;j++){
                char c=str.charAt(j);
                arr[i][j]=c;

                if(c=='o') sheep++;
                else if(c=='v') wolf++;
            }
        }

        for(int i=0;i<R;i++){
            for(int j=0;j<C;j++){
                if(arr[i][j]!='#'&&!visited[i][j]){
                    int[] count=bfs(i,j);
                    if(count[0]>count[1]) wolf-=count[1];
                    else sheep-=count[0];
                }
            }
        }

        System.out.println(sheep+" "+wolf);
    }

    static int[] bfs(int x, int y){
        int v=0;
        int o=0;

        Queue<Node> q=new LinkedList<>();
        q.offer(new Node(x,y));
        visited[x][y]=true;

        while(!q.isEmpty()){
            Node cur=q.poll();
            int px=cur.x;
            int py=cur.y;

            if(arr[px][py]=='o') o++;
            else if(arr[px][py]=='v') v++;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=R||ny<0||ny>=C||visited[nx][ny]) continue;

                if(arr[nx][ny]!='#'){
                    q.offer(new Node(nx,ny));
                    visited[nx][ny]=true;
                }
            }
        }

        return new int[]{o,v};
    }

    static class Node{
        int x, y;
        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
