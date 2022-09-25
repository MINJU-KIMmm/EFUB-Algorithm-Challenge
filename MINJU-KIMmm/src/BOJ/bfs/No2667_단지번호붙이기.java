package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No2667_단지번호붙이기 {
    static int N;
    static int[][]arr;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        arr=new int[N][N];
        visited=new boolean[N][N];
        for(int i=0;i<N;i++){
            String str=br.readLine();
            for(int j=0;j<N;j++){
                arr[i][j]=str.charAt(j)-'0';
            }
        }

        int type=0;
        ArrayList<Integer> list=new ArrayList<>();
        for(int i=0;i<N;i++){
            for(int j=0;j<N;j++){
                if(!visited[i][j]&&arr[i][j]==1){
                    visited[i][j]=true;
                    int size=bfs(i,j);
                    type++;
                    list.add(size);
                }
            }
        }

        System.out.println(type);
        Collections.sort(list);
        for(int num:list){
            System.out.println(num);
        }

    }

    static int bfs(int x, int y){
        Queue<Node> q=new LinkedList<>();
        q.add(new Node(x,y));
        visited[x][y]=true;

        int size=1;

        while(!q.isEmpty()){
            Node node=q.poll();
            int px=node.x;
            int py=node.y;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=N) continue;

                if(!visited[nx][ny]&&arr[nx][ny]==1){
                    size++;
                    q.offer(new Node(nx,ny));
                    visited[nx][ny]=true;
                }
            }
        }

        return size;
    }

    static class Node{
        int x, y;

        public Node(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
