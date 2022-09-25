package HackerRank.medium;

import java.util.*;
import java.io.*;
public class QueensAttack2 {
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx={-1,1,0,0,-1,1};
    static int[] dy={0,0,-1,1,1,-1};
    public static int queensAttack(int n, int k, int r_q, int c_q, List<List<Integer>> obstacles) {
        // Write your code here
       int u=n+1;
       int d=0;
       int left=0;
       int right=n+1;
       int ld=0, lu=n+1, rd=0, ru=n+1;

       int count=0;

       for(int i=0;i<obstacles.size();i++){
           int r_o=obstacles.get(i).get(0);
           int c_o=obstacles.get(i).get(1);

           if(r_q==r_o){
               //right
               if(c_q<c_o){
                   right=Math.min(right,c_o);
               }
               //left
               else{
                   left=Math.max(left, c_o);
               }
           }else if(c_q==c_o){
               //up
               if(r_q<r_o){
                   u=Math.min(u,r_o);
               }
               //down
               else{
                   d=Math.max(d, r_o);
               }
           }else{
               //기울기 1
               if(r_o-r_q==c_o-c_q){
                   //right up
                   if(r_q<r_o){
                       ru=Math.min(ru, r_o);
                   }
                   else{
                       ld=Math.max(ld, r_o);
                   }
               }
               else if(r_o-r_q==-(c_o-c_q)){
                   if(r_q<r_o){
                       lu=Math.min(lu, r_o);
                   }else{
                       rd=Math.max(rd, r_o);
                   }
               }
           }

           count+=(u-r_q-1);
           count+=(r_q-d-1);
           count+=(c_q-left-1);
           count+=(right-c_q-1);
           count+=Math.min((n+1)-c_q-1, ru-r_q-1);
           count+=Math.min(c_q-1, r_q-ld-1);
           count+=Math.min(c_q-1, lu-r_q-1);
           count+=Math.min((n+1)-c_q-1, r_q-rd-1);


       }
       return count;
    }

    static boolean check1(int x, int y, int r_q, int c_q){
        if(x==r_q) return true;
        return false;
    }
    static boolean check2(int x, int y, int r_q, int c_q){
        if(y==c_q) return true;
        return false;
    }
    static boolean check3(int x, int y, int r_q, int c_q){
        if(Math.abs(x-r_q)==Math.abs(y-c_q)) return true;
        return false;
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int r_q=sc.nextInt();
        int c_q=sc.nextInt();

        List<List<Integer>> list=new ArrayList<>();
        for(int i=0;i<k;i++){
            list.add(new ArrayList<>());
            list.get(i).add(sc.nextInt());
            list.get(i).add(sc.nextInt());
        }

        int count=queensAttack(n,k,r_q,c_q,list);
        System.out.println(count);
    }

}
