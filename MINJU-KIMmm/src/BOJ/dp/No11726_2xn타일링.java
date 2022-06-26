package BOJ.dp;

import java.io.*;
import java.util.*;
public class No11726_2xn타일링 {
    static int[]dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        dp=new int[n];

        dp[0]=1;
        if(n>1) dp[1]=2;
        for(int i=2;i<n;i++){
            dp[i]=(dp[i-2]+dp[i-1])%10007;
        }

        System.out.println(dp[n-1]);
    }

}
