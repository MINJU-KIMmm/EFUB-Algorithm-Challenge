package BOJ.dfs;

import java.util.*;
import java.io.*;
public class No1167_트리의지름 {
    static ArrayList<Node>[] arr;
    static boolean[] visited;
    static int V, maxIdx, maxSum;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        V=Integer.parseInt(br.readLine());

        arr=new ArrayList[V+1];
        for(int i=0;i<V+1;i++){
            arr[i]=new ArrayList<>();
        }

        for(int i=0;i<V;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int count=0;
            while(true){
                count++;
                int b=Integer.parseInt(st.nextToken());
                if(b==-1) break;

                int cost=Integer.parseInt(st.nextToken());

                arr[a].add(new Node(b,cost));
            }
        }

        visited=new boolean[V+1];
        visited[1]=true;
        dfs(1,0);

        visited=new boolean[V+1];
        visited[maxIdx]=true;
        dfs(maxIdx, 0);
        System.out.println(maxSum);
    }

    static void dfs(int idx, int sum){
        if(maxSum<sum){
            maxSum=sum;
            maxIdx=idx;
        }

        for(Node node:arr[idx]){
            if(!visited[node.end]){
                visited[node.end]=true;
                dfs(node.end, sum+node.cost);
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
