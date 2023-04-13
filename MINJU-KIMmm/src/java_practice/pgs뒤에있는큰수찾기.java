package java_practice;

import java.util.*;
public class pgs뒤에있는큰수찾기 {
    static class Solution {
        public int[] solution(int[] numbers) {
            int[] answer = new int[numbers.length];
            Arrays.fill(answer, -1);
            Stack<Integer> stack = new Stack<>();

            for(int i=numbers.length-1;i>=0;i--){
                int num = numbers[i];
                int big_num = -1;
                while(!stack.isEmpty()) {
                    if(stack.peek()<=num) {
                        stack.pop();
                    } else{
                        big_num = stack.peek();
                        break;
                    }
                }
                stack.add(num);
                answer[i] = big_num;
            }
            return answer;
        }
    }

}
