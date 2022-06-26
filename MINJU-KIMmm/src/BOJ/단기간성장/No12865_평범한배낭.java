package BOJ.단기간성장;

import java.util.*;
import java.io.*;
public class No12865_평범한배낭 {
    static int[][] arr;
    static Integer[][] dp;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int K=Integer.parseInt(st.nextToken());

        arr=new int[N][2];
        dp=new Integer[N][K+1];

        for(int i=0;i<N;i++){
            st=new StringTokenizer(br.readLine());
            arr[i][0]=Integer.parseInt(st.nextToken());
            arr[i][1]=Integer.parseInt(st.nextToken());
        }

        System.out.println(solution(N-1,K));
    }

    static int solution(int i, int k){
        if(i<0) return 0;

        if(dp[i][k]==null){
            if(arr[i][0]>k){
                dp[i][k]=solution(i-1, k);
            }
            else{
                dp[i][k]=Math.max(solution(i-1,k-arr[i][0])+arr[i][1], solution(i-1, k));
            }
        }

        return dp[i][k];
    }
}
