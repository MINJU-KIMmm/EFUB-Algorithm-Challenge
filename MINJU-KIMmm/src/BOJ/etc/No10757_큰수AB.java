package BOJ.etc;

import java.math.BigInteger;
import java.util.*;
import java.io.*;
public class No10757_큰수AB {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st=new StringTokenizer(br.readLine());
        BigInteger A=new BigInteger(st.nextToken());
        BigInteger B=new BigInteger(st.nextToken());

        System.out.println(A.add(B));
    }
}
