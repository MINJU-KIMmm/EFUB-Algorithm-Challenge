package BOJ.sorting;

import java.util.*;
import java.io.*;
public class No1026_보물 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());
        int[] A=new int[N];
        StringTokenizer st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            A[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(A);

        Integer[] B=new Integer[N];
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<N;i++){
            B[i]=Integer.parseInt(st.nextToken());
        }

        Arrays.sort(B, Collections.reverseOrder());

        int S=0;
        for(int i=0;i<N;i++){
            S+=(A[i]*B[i]);
        }

        System.out.println(S);
    }
}
