package BOJ.dp;

import java.util.*;
import java.io.*;
public class No22971_증가하는부분수열의개수 {
    static int[] dp=new int[5001];
    static int MOD=998244353;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int N=Integer.parseInt(br.readLine());
        int[] arr=new int[N+1];
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=1;i<=N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        for(int i=1;i<=N;i++){
            dp[i]=1;
            for(int j=0;j<i;j++){
                if(arr[i]>arr[j]) {
                    dp[i] =(dp[i]+dp[j])%MOD;
                }
            }
        }

        for(int i=1;i<=N;i++){
            System.out.print(dp[i]%MOD+" ");
        }
    }
}
