package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No10819_차이를최대로 {
    static int answer=Integer.MIN_VALUE;
    static int[] arr;
    static int[] caseArr;
    static int N;
    static boolean[] visited;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        N=Integer.parseInt(br.readLine());
        arr=new int[N];
        visited=new boolean[N];
        caseArr=new int[N];

        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        solution(0);
        System.out.println(answer);
    }

    static void solution(int cnt){
        if(cnt==N){
            int sum=0;
            for(int i=0;i<N-1;i++){
                sum+=Math.abs(caseArr[i]-caseArr[i+1]);
            }
            answer=Math.max(answer, sum);
            return;
        }

        for(int i=0;i<N;i++){
            if(!visited[i]){
                visited[i]=true;
                caseArr[cnt]=arr[i];
                solution(cnt+1);
                visited[i]=false;
            }
        }
    }

}
