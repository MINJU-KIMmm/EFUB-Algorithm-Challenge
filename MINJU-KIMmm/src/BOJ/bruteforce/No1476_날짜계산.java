package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No1476_날짜계산 {
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int E=Integer.parseInt(st.nextToken())%15; //15
        int S=Integer.parseInt(st.nextToken())%28; //28
        int M=Integer.parseInt(st.nextToken())%19; //19

        int year=1;
        while(true){
            int e=year%15;
            int s=year%28;
            int m=year%19;

            if(e==E&&s==S&&m==M) break;

            year++;
        }

        System.out.println(year);
    }
}
