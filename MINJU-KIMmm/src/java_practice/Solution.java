package java_practice;

import java.util.*;
class Solution {
    static class Node implements Comparable<Node>{
        int node;
        int cost;

        public Node(int node, int cost){
            this.node = node;
            this.cost = cost;
        }


        @Override
        public int compareTo(Node o1) {
            if(this.cost<o1.cost){
                return -1;
            }else{
                return 1;
            }
        }
    }
    public int solution(int n, int[][] costs) {
        int answer = 0;

        ArrayList<Node>[] connect = new ArrayList[costs.length];
        for(int i=0;i<costs.length;i++){
            connect[i] = new ArrayList<Node>();
        }

        for(int i=0;i<costs.length;i++){
            int a = costs[i][0];
            int b = costs[i][1];
            int c = costs[i][2];

            connect[a].add(new Node(b, c));
            connect[b].add(new Node(a, c));
        }

        for(int i=0;i<costs.length;i++){
            Collections.sort(connect[i], new Comparator<Node>() {
                @Override
                public int compare(Node o1, Node o2) {
                    if(o1.cost<o2.cost){
                        return -1;
                    } else{
                        return 1;
                    }
                }
            });
        }

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(0, 0));

        boolean[] visited = new boolean[n];
        visited[0] = true;

        while(!pq.isEmpty()){
            Node now = pq.poll();

            if(visited[now.node]) continue;

            visited[now.node] = true;
            answer += now.cost;

            for(Node next:connect[now.node]){
                pq.add(next);
            }
        }

        return answer;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(4, new int[][]{{0,1,1},{0,2,2},{1,2,5},{1,3,1},{2,3,8}});
    }
}