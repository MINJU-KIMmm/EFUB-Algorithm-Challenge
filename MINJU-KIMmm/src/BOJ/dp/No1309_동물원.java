package BOJ.dp;

import java.util.*;
import java.io.*;
public class No1309_동물원 {
    static int[][] dp;
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        dp=new int[N+1][3];
        Arrays.fill(dp[1],1);

        //dp[i][0] : i번째 방에 사자 넣지 않는 경우
        //  -> 이전 방이 어떤 경우여도 상관 없음
        //dp[i][1] : i번째 방의 왼쪽에 사자 넣는 경우
        //  -> 이전 방의 왼쪽에 사자가 올 수 없음
        //dp[i][2] : i번째 방의 오른쪽에 사자 넣는 경우
        //  -> 이전 방의 오른쪽에 사자가 올 수 없음
        for(int i=2;i<=N;i++){
            dp[i][0]=(dp[i-1][0]+dp[i-1][1]+dp[i-1][2])%9901;
            dp[i][1]=(dp[i-1][0]+dp[i-1][2])%9901;
            dp[i][2]=(dp[i-1][0]+dp[i-1][1])%9901;
        }

        //최종 방인 N번째 방들의 경우의 수를 더하여 최종 경우의 수를 구해준다.
        System.out.println((dp[N][0]+dp[N][1]+dp[N][2])%9901);
    }
}
