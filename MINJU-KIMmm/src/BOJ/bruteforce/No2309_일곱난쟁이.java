package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No2309_일곱난쟁이 {
    static int[] arr=new int[9];
    static boolean[] check=new boolean[9];
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int sum=0;
        for(int i=0;i<9;i++){
            arr[i]=Integer.parseInt(br.readLine());
            sum+=arr[i];
        }

        Arrays.sort(arr);
        int fake1=0, fake2=0;
        for(int i=0;i<8;i++){
            for(int j=i+1;j<9;j++){
                if(sum-arr[i]-arr[j]==100){
                    fake1=arr[i];
                    fake2=arr[j];
                }
            }
        }

        for(int i=0;i<9;i++){
            if(arr[i]!=fake1&&arr[i]!=fake2) System.out.println(arr[i]);
        }
    }

}
