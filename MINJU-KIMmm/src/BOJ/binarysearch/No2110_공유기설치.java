package BOJ.binarysearch;

import java.util.*;
import java.io.*;
public class No2110_공유기설치 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int C=Integer.parseInt(st.nextToken());

        int[] arr=new int[N];
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(br.readLine());
        }

        Arrays.sort(arr);

        int left=1;
        int right=arr[arr.length-1]-arr[0];

        int dist=0;
        int answer=0;
        while(left<=right){
            int mid=(left+right)/2;
            int compare=arr[0];
            int installed=1;

            for(int i=1;i<N;i++){
                dist=arr[i]-compare;
                if(dist>=mid){
                    installed++;
                    compare=arr[i];
                }
            }

            if(installed>=C){
                answer=mid;
                left=mid+1;
            }
            else{
                right=mid-1;
            }
        }

        System.out.println(answer);
    }
}
