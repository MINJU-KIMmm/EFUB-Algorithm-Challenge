package BOJ.string;

import java.util.*;
import java.io.*;
public class No11656_접미사배열 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String S=br.readLine();

        ArrayList<String> arr=new ArrayList<>();

        for(int i=0;i<S.length();i++){
            arr.add(S.substring(i));
        }

        Collections.sort(arr);

        for(int i=0;i<arr.size();i++){
            System.out.println(arr.get(i));
        }

    }
}
