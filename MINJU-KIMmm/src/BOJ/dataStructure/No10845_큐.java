package BOJ.dataStructure;

import java.util.*;
import java.io.*;
public class No10845_큐 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int N=Integer.parseInt(br.readLine());

        Queue<Integer> q=new LinkedList<>();

        while(N-->0) {
            StringTokenizer st=new StringTokenizer(br.readLine());
            String command=st.nextToken();

            switch(command){
                case "push":
                    int num=Integer.parseInt(st.nextToken());
                    q.add(num);
                    break;
                case "pop":
                    if(q.isEmpty()){
                        System.out.println(-1);
                    }
                    else {
                        System.out.println(q.poll());
                    }
                    break;
                case "size":
                    System.out.println(q.size());
                    break;
                case "empty":
                    if(q.isEmpty()){
                        System.out.println(1);
                    }else{
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if(q.isEmpty()){
                        System.out.println(-1);
                    }
                    else{
                        System.out.println(q.peek());
                    }
                    break;
                case "back":
                    if(q.isEmpty()){
                        System.out.println(-1);
                    }
                    else{
                        ArrayList<Integer> arr=new ArrayList<>(q);
                        System.out.println(arr.get(arr.size()-1));
                    }
                    break;
            }
        }
    }
}
