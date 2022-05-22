package BOJ.prefixSum;

import java.util.*;
import java.io.*;
public class No11660_구간합구하기5 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        //열단위로 누적
        //간편한 계산을 위해 배열크기 N+1로 선언
        int[][] arr=new int[N+1][N+1];
        for(int i=1;i<=N;i++){
            st=new StringTokenizer(br.readLine());
            for(int j=1;j<=N;j++){
                arr[i][j]=Integer.parseInt(st.nextToken())+arr[i-1][j];
            }
        }

        int[] answer=new int[M];
        for(int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            int x1=Integer.parseInt(st.nextToken());
            int y1=Integer.parseInt(st.nextToken());
            int x2=Integer.parseInt(st.nextToken());
            int y2=Integer.parseInt(st.nextToken());

            //열단위로 계산
            //열단위로 누적합 이용
            for(int col=y1;col<=y2;col++){
                answer[i]+=arr[x2][col]-arr[x1-1][col];
            }
        }

        for(int ans:answer){
            System.out.println(ans);
        }
    }
}
