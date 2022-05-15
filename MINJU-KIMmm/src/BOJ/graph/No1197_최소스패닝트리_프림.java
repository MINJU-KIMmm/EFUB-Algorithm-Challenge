package BOJ.graph;

import java.util.*;
import java.io.*;
public class No1197_최소스패닝트리_프림 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

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
    }

}
