package BOJ.bfs;

import java.util.*;
import java.io.*;
public class No16953_AB {
    static int count=1;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int A=Integer.parseInt(st.nextToken());
        int B=Integer.parseInt(st.nextToken());


        while(B!=A){
            if(B<A){
                count=-1;
                break;
            }

            if(B%10!=1&&B%2!=0){
                count=-1;
                break;
            }

            String str=Integer.toString(B);

            if(B%2==0){
                B/=2;
            }else{
                str=str.substring(0,str.length()-1);
                B=Integer.parseInt(str);
            }

            count++;
        }

        System.out.println(count);
    }


}
