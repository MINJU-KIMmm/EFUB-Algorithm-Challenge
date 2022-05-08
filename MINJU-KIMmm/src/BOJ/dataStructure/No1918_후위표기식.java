package BOJ.dataStructure;

import java.util.*;
import java.io.*;
public class No1918_후위표기식 {
    public static void main(String[] args)throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        String input=br.readLine();

        Stack<Character> stack=new Stack<>();
        StringBuilder sb=new StringBuilder();

        for(int i=0;i<input.length();i++){
            char c=input.charAt(i);
            if(c=='+'||c=='*'||c=='-'||c=='/'){
                while(!stack.isEmpty()&&priority(c)<=priority(stack.peek())){
                    sb.append(stack.pop());
                }
                stack.push(c);
            }
            else if(c=='('){
                stack.push(c);
            }
            else if(c==')'){
                while(!stack.isEmpty()&&stack.peek()!='('){
                    sb.append(stack.pop());
                }
                stack.pop();
            }
            else{
                sb.append(c);
            }
        }

        while(!stack.isEmpty()){
            sb.append(stack.pop());
        }

        System.out.println(sb);
    }

    static int priority(char c){
        if(c=='('||c==')') return 0;
        if(c=='+'||c=='-') return 1;
        if(c=='*'||c=='/') return 2;
        return -1;
    }
}
