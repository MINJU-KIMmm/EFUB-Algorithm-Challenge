package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No1182_부분수열의합 {
    static int N,S;
    static int cnt=0;
    static int[] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        N=Integer.parseInt(st.nextToken());
        S=Integer.parseInt(st.nextToken());

        arr=new int[N];
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
        }

        solution(0,0);
        System.out.println(S==0? cnt-1:cnt); //공집합을 빼준다.

    }

    static void solution(int start, int sum){
        if(start==N) {
            if (sum == S) {
                cnt++;
            }
            return;
        }

        solution(start+1, sum+arr[start]);
        solution(start+1, sum);
    }
}
