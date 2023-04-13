package java_practice;

import java.util.*;
public class pgs혼자서하는틱택토 {
    class Node{
        int x;
        int y;

        public Node(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    class Solution {
        public int solution(String[] board) {
            int answer = -1;
            ArrayList<Node> O_list = new ArrayList<>();
            ArrayList<Node> X_list = new ArrayList<>();

            for(int i=0;i<3;i++) {
                for(int j=0;j<3;j++){
                    if(board[i].charAt(j)=='O'){
                        O_list.add(new Node(i,j));
                    }
                    if(board[i].charAt(j)=='X'){
                        X_list.add(new Node(i,j));
                    }
                }
            }

            if(O_list.size() != X_list.size()){
                return 0;
            }

            int[] osame_row = new int[3];
            int[] osame_col = new int[3];
            for(int i=0;i<O_list.size();i++) {
                osame_row[O_list.get(i).x]++;
                osame_col[O_list.get(i).y]++;
            }


            int []xsame_row = new int[3];
            int[] xsame_col = new int[3];
            for(int i=0;i<X_list.size();i++){
                xsame_row[X_list.get(i).x]++;
                xsame_col[X_list.get(i).y]++;
            }

            int row = 1, col =1;
            boolean flag = false;
            while(row<3 && col<3){
                if(board[row].charAt(col)!=board[row-1].charAt(col-1)) flag = true;
                row++;
                col++;
            }

            row = 1;
            col = 1;
            while(row<3 && col>-1){
                if(board[row].charAt(col)!=board[row-1].charAt(col+1)) flag = true;
                row++;
                col++;
            }

            if(!flag){
                return 0;
            }

            return 1;
//            int [] dx = {1, 0, 1, -1};
//            int [] dy = {0, 1, 1, 1};
//            int O_count = 0;
//            int X_count = 0;
//            //가로 세로 체크
//            for(int i=0;i<3;i++) {
//                char who1 = board[i].charAt(0);
//                char who2 = board[0].charAt(i);
//                int count1 = 0;
//                int count2 = 0;
//                for(int j=0;j<3;j++) {
//                    if(who1==board[i].charAt(0)){
//                        count1 ++ ;
//                    }
//                    if(who2==board[j].charAt(i)){
//                        count2++;
//                    }
//
//                    if(board[i].charAt(0)=='O') O_count++;
//                    if(board[i].charAt(j))
//                }
//
//                if(count1==3||count2==3){
//                    return 0;
//                }
//            }
//
//            for(int i=0;i<3;i++){
//                for(int j=0;j<3;j++){
//                    if()
//                }
//            }
        }
    }

    public static void main(String[] args) {

    }
}
