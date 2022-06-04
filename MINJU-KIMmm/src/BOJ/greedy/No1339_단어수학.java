package BOJ.greedy;

import java.util.*;
import java.io.*;
public class No1339_단어수학 {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        int N=sc.nextInt();
        String[] arr=new String[N];
        int[] value=new int[26];
        for(int i=0;i<N;i++){
            arr[i]=sc.next();
        }

        //자릿수 계산
        for(int i=0;i<N;i++){
            int temp=(int)Math.pow(10,arr[i].length()-1);
            for(int j=0;j<arr[i].length();j++){
                value[arr[i].charAt(j)-65]+=temp;
                temp/=10;
            }
        }

        Arrays.sort(value);
        int num=9;
        int sum=0;

        //자릿수가 높으면 높은 숫자 부여
        for(int i=value.length-1;i>=0;i--){
            if(value[i]==0) break ;
            sum+=value[i]*num;
            num--;
        }

        System.out.println(sum);
    }
}
