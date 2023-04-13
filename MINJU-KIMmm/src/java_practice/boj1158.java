package java_practice;

import java.util.*;
import java.io.*;
public class boj1158 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        Queue<Integer> q = new LinkedList<>();
        int count = 0;
        List<Integer> answer = new ArrayList<>();

        for(int i=1;i<=N;i++) {
            if(i%K==0) {
                count = 0;
                answer.add(i);
            }
            else {
                q.add(i);
                count += 1;
            }
        }

        while(!q.isEmpty()) {
            int next = q.poll();
            count += 1;
            if(count==K) {
                answer.add(next);
                count = 0;
            }
            else{
                q.add(next);
            }
        }

        System.out.print("<");
        for(int i=0;i<answer.size()-1;i++) {
            System.out.print(answer.get(i)+", ");
        }
        System.out.println(answer.get(answer.size()-1)+">");
    }
}
