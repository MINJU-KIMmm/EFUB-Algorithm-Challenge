package BOJ.string;

import java.util.*;
import java.io.*;
public class No11721_열개씩끊어출력하기 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String str=br.readLine();

        int cnt=0;
        int len=str.length()/10;
        for(int i=0;i<len;i++){
            System.out.println(str.substring(i*10, i*10+10));
        }
        System.out.println(str.substring(len*10));
    }
}
