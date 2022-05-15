package BOJ.prefixSum;

import java.util.*;
import java.io.*;
public class No11659_구간합구하기4 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        int[] arr=new int[N];
        st=new StringTokenizer(br.readLine());

        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
            if(i!=0){
                arr[i]+=arr[i-1];
            }
        }

        int[] answer=new int[M];
        for(int m=0;m<M;m++){
            st=new StringTokenizer(br.readLine());
            int i=Integer.parseInt(st.nextToken())-1;
            int j=Integer.parseInt(st.nextToken())-1;

            if(i==0){
                answer[m]=arr[j];
            }
            else{
                answer[m]=(arr[j]-arr[i-1]);
            }
        }

        for(int ans:answer){
            System.out.println(ans);
        }
    }

}
