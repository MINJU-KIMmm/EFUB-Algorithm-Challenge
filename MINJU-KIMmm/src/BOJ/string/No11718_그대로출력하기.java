package BOJ.string;

import java.util.*;
import java.io.*;
public class No11718_그대로출력하기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        String str="";
        //입력 횟수 안 받고 입력 끝나면 끝낼 수 있도록
        while((str=br.readLine())!=null){
            System.out.println(str);
        }
    }
}
