package BOJ.greedy;

import java.util.*;
import java.io.*;

//1. 처음에 sum이 우선순위 큐에 들어간다고 생각해서 틀림
//2. 남은 카드셋이 1개인 경우에도 카드를 비교해야 한다고 생각해서 틀림
public class No1715_카드정렬하기 {
    public static void main(String[] args) throws IOException{
        Scanner sc=new Scanner(System.in);
        int N=sc.nextInt();
        PriorityQueue<Integer> q=new PriorityQueue<>();

        for(int i=0;i<N;i++){
            q.add(sc.nextInt());
        }


        int sum=0;
        //우선순위큐에 있는 카드셋이 하나라면 비교하지 않아도 된다
        while(q.size()>1){
            int a=q.poll();
            int b=q.poll();
            sum+=(a+b);
            q.add(a+b); //현재 더한 값이 q에 들어가야 함
        }

        System.out.println(sum);
    }
}
