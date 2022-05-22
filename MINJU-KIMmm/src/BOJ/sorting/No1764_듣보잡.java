package BOJ.sorting;


import java.util.*;
import java.io.*;

public class No1764_듣보잡 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int N=Integer.parseInt(st.nextToken());
        int M=Integer.parseInt(st.nextToken());

        HashSet<String> hear=new HashSet<>();
        for(int i=0;i<N;i++){
            hear.add(br.readLine());
        }

        int cnt=0;
        ArrayList<String> two=new ArrayList<>();
        for(int i=0;i<M;i++){
            String name=br.readLine();
            if(hear.contains(name)){
                two.add(name);
                cnt++;
            }
        }

        Collections.sort(two);
        System.out.println(cnt);
        for(String name:two){
            System.out.println(name);
        }
    }



}
