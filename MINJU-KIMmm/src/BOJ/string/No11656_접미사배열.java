package BOJ.string;

import java.util.*;
import java.io.*;
public class No11656_접미사배열 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String S=br.readLine();

        HashSet<String> set=new HashSet<>();

        StringBuilder sb=new StringBuilder();
        for(int i=S.length()-1;i>=0;i--){
            sb.append(S.charAt(i));
            sb.reverse();
            set.add(sb.toString());
            sb.reverse();
        }

        ArrayList<String> arr=new ArrayList<>(set);
        Collections.sort(arr);

        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }

    }
}
