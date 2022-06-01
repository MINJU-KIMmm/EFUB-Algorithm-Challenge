package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No16953_AB_bfs {
    static int A,B;
    static HashMap<Long, Integer> map=new HashMap<>();
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        A=Integer.parseInt(st.nextToken());
        B=Integer.parseInt(st.nextToken());

        int cnt=bfs();
        System.out.println(cnt+1);
    }

    public static int bfs(){
        Queue<Node> q=new LinkedList<>();
        q.add(new Node(A,0));
        while(!q.isEmpty()){
            Node cur=q.poll();
            if(cur.val==B){
                return cur.cnt;
            }
            if(cur.val*2<=B&&!map.containsKey(cur.val*2)){
                map.put(cur.val*2, cur.cnt+1);
                q.add(new Node(cur.val*2, cur.cnt+1));
            }
            if(cur.val*10+1<=B&&!map.containsKey(cur.val*10+1)){
                map.put(cur.val*10+1, cur.cnt+1);
                q.add(new Node(cur.val*10+1, cur.cnt+1));
            }
        }

        return -2;
    }

    static class Node{
        long val;
        int cnt;
        public Node(long val, int cnt){
            this.val=val;
            this.cnt=cnt;
        }
    }
}
