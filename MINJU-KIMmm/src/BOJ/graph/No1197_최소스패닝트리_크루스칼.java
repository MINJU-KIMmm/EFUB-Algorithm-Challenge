package BOJ.graph;

import java.util.*;
import java.io.*;
public class No1197_최소스패닝트리_크루스칼 {
    static int[] parent;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int V=Integer.parseInt(st.nextToken());
        int E=Integer.parseInt(st.nextToken());

        ArrayList<Edge> edges=new ArrayList<>();
        int answer=0;

        for(int i=0;i<E;i++){
            st=new StringTokenizer(br.readLine());
            int start=Integer.parseInt(st.nextToken());
            int end=Integer.parseInt(st.nextToken());
            int cost=Integer.parseInt(st.nextToken());

            edges.add(new Edge(start, end, cost));
        }

        //cost 기준으로 정렬(or 우선순위큐 써줘도 됨)
        edges.sort(new Comparator<Edge>(){
            @Override
            public int compare(Edge o1, Edge o2) {
                return Integer.compare(o1.c, o2.c);
            }
        });

        //parent 초기화
        //처음에는 자기자신을 root로 가지도록 설정
        parent=new int[V+1];
        for(int i=1;i<V+1;i++){
            parent[i]=i;
        }

        //트리 계산
        //isSameParent==true -> cycle 발생
        //false인 경우 cost를 answer에 합산 한 후, 한 트리로 union
        for(int i=0;i<E;i++){
            Edge edge=edges.get(i);
            if(!isSameParent(edge.s, edge.e)){
                answer+=edge.c;
                union(edge.s, edge.e);
            }
        }

        System.out.println(answer);

    }

    //parent 찾기
    static int findParent(int x){
        //루트가 아니면 재귀로 parent 찾기
        if(parent[x]!=x){
            parent[x]=findParent(parent[x]);
        }
        return parent[x];
    }

    //같은 parent인지 판별
    static boolean isSameParent(int x, int y){
        x=findParent(x);
        y=findParent(y);

        if(x==y)return true;
        else return false;
    }

    //Union
    static void union(int x, int y){
        x=findParent(x);
        y=findParent(y);

        if(x<y){
            parent[y]=x;
        }
        else{
            parent[x]=y;
        }
    }
}

class Edge{
    int s, e, c;
    Edge(int s, int e, int c){
        this.s=s;
        this.e=e;
        this.c=c;
    }
}
