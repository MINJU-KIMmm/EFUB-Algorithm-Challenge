package BOJ.dp;

import java.util.*;
import java.io.*;
public class No2193_이친수 {
    static long[] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        dp=new long[N+1];
        dp[1]=1;
        if(N>=2) dp[2]=1;

        for(int i=3;i<=N;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }

        System.out.println(dp[N]);
    }
}
