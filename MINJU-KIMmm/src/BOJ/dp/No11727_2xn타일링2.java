package BOJ.dp;

import java.util.*;
import java.io.*;
public class No11727_2xn타일링2 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());

        long[] dp=new long[n];
        dp[0]=1;
        if(n>=2){
            dp[1]=3;
        }
        for(int i=2;i<n;i++){
            dp[i]=(dp[i-2]+dp[i-2]+dp[i-1])%10007;
        }

        System.out.println(dp[n-1]);
    }
}
