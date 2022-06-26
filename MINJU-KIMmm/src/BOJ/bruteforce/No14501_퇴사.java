package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No14501_퇴사 {
    static Plan[] arr;
    static int N;
    static int answer;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        N=Integer.parseInt(br.readLine());

        arr=new Plan[N];
        for(int i=0;i<N;i++){
            StringTokenizer st=new StringTokenizer(br.readLine());
            arr[i]=new Plan(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        int[] dp=new int[N+1];
        for(int i=0;i<N;i++){
            if(arr[i].day+i<=N){
                dp[arr[i].day+i]=Math.max(dp[arr[i].day+i], dp[i]+arr[i].prop);
            }
            dp[i+1]=Math.max(dp[i+1], dp[i]); //이전 상담 금액 유지(해당 날짜의 상담을 할 수 없는 경우 이전까지 일한 최대 수당 입력)
        }

        System.out.println(dp[N]);
    }

    static class Plan{
        int day, prop;

        public Plan(int day, int prop){
            this.day=day;
            this.prop=prop;
        }
    }
}
