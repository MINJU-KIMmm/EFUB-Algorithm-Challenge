package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No16234_인구이동 {
    static int[][] A;
    static int[] dx={-1,1,0,0};
    static int[] dy={0,0,-1,1};
    static boolean[][] visited;
    static int N, L, R;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        L=Integer.parseInt(st.nextToken());
        R=Integer.parseInt(st.nextToken());

        A=new int[N][N];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                A[i][j]=Integer.parseInt(st.nextToken());
            }
        }

        int day=0;
        while(true){
            visited=new boolean[N][N];

            boolean turn=false; //인구 이동 더이상 하는지 안하는지 검사

            for(int i=0;i<N;i++){
                for(int j=0;j<N;j++){
                    //방문하지 않은 경우(이거 꼭 있어야 함)
                    if(!visited[i][j]) {
                        ArrayList<Nation> list = bfs(i, j);
                        //연합 국가 있는 경우
                        if (list.size() > 1) {
                            calc(list); //계산
                            turn = true;
                        }
                    }
                }
            }

            //연합국가 더이상 없으면 break
            if(!turn) break;
            //있으면 날짜 증가
            else day++;
        }

        System.out.println(day);
    }

    static ArrayList<Nation> bfs(int x, int y){
        Queue<Nation> q=new LinkedList<>();
        q.offer(new Nation(x,y));
        visited[x][y]=true;

        ArrayList<Nation> list=new ArrayList<>();
        list.add(new Nation(x,y));
        while(!q.isEmpty()){
            Nation nation=q.poll();
            int px=nation.x;
            int py=nation.y;

            for(int i=0;i<4;i++){
                int nx=px+dx[i];
                int ny=py+dy[i];

                if(nx<0||nx>=N||ny<0||ny>=N||visited[nx][ny]) continue;

                if(checkUnion(nation, new Nation(nx,ny), L, R)){
                    list.add(new Nation(nx,ny));
                    q.offer(new Nation(nx,ny));
                    visited[nx][ny]=true;
                }
            }
        }

        return list;
    }
    static boolean checkUnion(Nation n1, Nation n2, int L, int R){
        int x1=n1.x;
        int x2=n2.x;
        int y1=n1.y;
        int y2=n2.y;

        int diff=Math.abs(A[x1][y1]-A[x2][y2]);

        return diff>=L&&diff<=R;
    }

    static void calc(ArrayList<Nation> list){
        int sum=0;
        for(int i=0;i<list.size();i++){
            sum+=A[list.get(i).x][list.get(i).y];
        }
        sum/=list.size();
        for(Nation n:list){
            A[n.x][n.y]=sum;
        }
    }

    static class Nation{
        int x,y;
        public Nation(int x, int y){
            this.x=x;
            this.y=y;
        }
    }
}
