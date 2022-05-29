package BOJ.graph;

import java.io.*;
import java.util.*;

//하나의 시작점으로부터 최단경로 찾기 -> 다익스트라 알고리즘
public class No1753_최단경로 {
    static final int INF=(int)1e9;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int V=Integer.parseInt(st.nextToken());
        int E=Integer.parseInt(st.nextToken());

        int K=Integer.parseInt(br.readLine());

        List<Edge>[] arr=new ArrayList[V+1];

        for(int i=0;i<=V;i++){
            arr[i]=new ArrayList<>();
        }

        for(int i=0;i<E;i++){
            st=new StringTokenizer(br.readLine());
            int u=Integer.parseInt(st.nextToken());
            int v=Integer.parseInt(st.nextToken());
            int w=Integer.parseInt(st.nextToken());

            arr[u].add(new Edge(v,w));
        }

        int[] dist=new int[V+1];
        boolean[] visited=new boolean[V+1];

        Arrays.fill(dist, INF);
        dist[K]=0; // 시작점 설정

        PriorityQueue<Edge> pq=new PriorityQueue<>();
        pq.add(new Edge(K, 0));

        while(!pq.isEmpty()){
            Edge cur=pq.poll();
            if(visited[cur.v]) continue;

            //이어서 오는 정점 거쳐가기 vs 안 거쳐가기 비교해서 더 작은 값으로 dist 설정
            for(Edge next:arr[cur.v]){
                if(!visited[next.v]&&dist[next.v]>dist[cur.v]+next.w){
                    dist[next.v]=dist[cur.v]+next.w;
                    pq.add(new Edge(next.v, dist[next.v]));
                }
            }

            visited[cur.v]=true;
        }

        for(int i=1;i<dist.length;i++){
            if(dist[i]==INF) System.out.println("INF");
            else System.out.println(dist[i]);
        }
    }

    static class Edge implements Comparable<Edge>{
        int v,w;

        public Edge(int v, int w){
            this.v=v;
            this.w=w;
        }

        @Override
        public int compareTo(Edge o){
            return Integer.compare(this.w, o.w);
        }
    }
}
