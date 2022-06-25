package BOJ.bruteforce;


import java.util.*;
import java.io.*;
public class No15686_치킨배달 {
    static int[][] arr;
    static ArrayList<Node> home=new ArrayList<>();
    static ArrayList<Node> chicken=new ArrayList<>();
    static int answer=0;
    static boolean[] open;
    static int N,M;
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        N=Integer.parseInt(st.nextToken());
        M=Integer.parseInt(st.nextToken());

        arr=new int[N][N];
        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=0;j<N;j++){
                arr[i][j]=Integer.parseInt(st.nextToken());
                if(arr[i][j]==1) home.add(new Node(i,j));
                else if(arr[i][j]==2) chicken.add(new Node(i,j));
            }
        }

        answer=Integer.MAX_VALUE;
        open=new boolean[chicken.size()];

        dfs(0,0);
        System.out.println(answer);
    }

    static void dfs(int start, int count){
        if(count==M){
            int minTotal=0;

            for(int i=0;i<home.size();i++){
                int minDist=Integer.MAX_VALUE;
                for(int j=0;j<chicken.size();j++){
                    if(open[j]) {
                        int dist = Math.abs(home.get(i).x - chicken.get(j).x) + Math.abs(home.get(i).y - chicken.get(j).y);
                        minDist = Math.min(dist, minDist);
                    }
                }
                minTotal+=minDist;
            }

            answer=Math.min(minTotal, answer);
            return;
        }

        for(int i=start;i<chicken.size();i++){
            open[i]=true;
            dfs(i+1, count+1);
            open[i]=false;
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
