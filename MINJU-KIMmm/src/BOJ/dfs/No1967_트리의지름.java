package BOJ.dfs;

import java.util.*;
import java.io.*;
public class No1967_트리의지름 {
    static int n, maxSum, maxIdx;
    static ArrayList<Node>[] arr;
    static boolean[] visited;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        n=Integer.parseInt(br.readLine());

        arr=new ArrayList[n+1];
        for(int i=0;i<n+1;i++){
            arr[i]=new ArrayList<>();
        }

        for(int i=0;i<n-1;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());
            int cost=Integer.parseInt(st.nextToken());

            arr[a].add(new Node(b,cost));
            arr[b].add(new Node(a,cost));
        }


        visited=new boolean[n+1];

        visited[1]=true;
        dfs(1,0);

        visited=new boolean[n+1];
        visited[maxIdx]=true;
        dfs(maxIdx, 0);
        System.out.println(maxSum);
    }


    static void dfs(int x, int cost){
        if(maxSum<cost){
            maxSum=cost;
            maxIdx=x;
        }

        for(Node node:arr[x]){
            if(!visited[node.end]){
                visited[node.end]=true;
                dfs(node.end, cost+node.cost);
            }
        }
    }

    static class Node{
        int end, cost;

        public Node(int end, int cost){
            this.end=end;
            this.cost=cost;
        }
    }
}
