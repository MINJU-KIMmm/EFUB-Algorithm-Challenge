package BOJ.graph;

import java.util.*;
import java.io.*;

//dfs를 사용하여 트리의 부모를 찾는다
public class No11725_트리의부모찾기 {
    static ArrayList<Integer>[] arr; //연결상태를 저장할 리스트배열
    static int[] parent; //노드의 parent를 저장할 배열 ex) 1의 부모 : parent[1]
    static boolean[] visited; //dfs 탐색에서 방문 여부 확인하기 위한 배열
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        //배열 초기화
        parent=new int[N+1];
        visited=new boolean[N+1];

        arr=new ArrayList[N+1];
        for(int i=1;i<N+1;i++){
            arr[i]=new ArrayList<>();
        }

        //노드 연결하기(양방향으로 연결)
        for(int i=0;i<N-1;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());

            arr[a].add(b);
            arr[b].add(a);
        }

        //dfs 탐색
        //이미 방문한 경우에는 방문하지 않는다(이미 부모 지정)
        for(int i=1;i<N+1;i++){
            if(!visited[i]){
                dfs(i);
            }
        }

        //출력
        for(int i=2;i<N+1;i++){
            System.out.println(parent[i]);
        }
    }

    //dfs
    //arr[i]에 연결된 노드들에 parent값을 i로 설정하고 그 노드들에 대해 dfs 탐색 진행
    static void dfs(int i){
        if(visited[i]) return;

        visited[i]=true;
        for(int num:arr[i]){
            if(!visited[num]){
                parent[num]=i;
                dfs(num);
            }
        }
    }
}
