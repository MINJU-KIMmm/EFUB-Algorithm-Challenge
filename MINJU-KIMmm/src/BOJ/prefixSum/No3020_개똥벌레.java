package BOJ.prefixSum;

import java.util.*;
import java.io.*;
public class No3020_개똥벌레 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken()); // 항상 짝수
        int H=Integer.parseInt(st.nextToken());

        int[] bottom=new int[H+1]; //석순
        int[] top=new int[H+1]; //종유석
        for(int i=0;i<N;i++){
            int num=Integer.parseInt(br.readLine());
            if(i%2==0) bottom[num]++;
            else top[num]++;
        }

        for(int i=H;i>0;i--){
            bottom[i-1]+=bottom[i];
            top[i-1]+=top[i];
        }

        int min=N;
        int cnt=1;
        for(int i=1;i<=H;i++){
            int crush=bottom[i]+top[H-i+1];
            if(crush<min){
                min=crush;
                cnt=1;
            }
            else if(crush==min){
                cnt++;
            }
        }

        System.out.println(min+" "+cnt);
    }
}
