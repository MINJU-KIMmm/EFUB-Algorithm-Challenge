package BOJ.bruteforce;

import java.util.*;
import java.io.*;
public class No1756_암호만들기 {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int L=Integer.parseInt(st.nextToken());
        int C=Integer.parseInt(st.nextToken());

        String[] arr=new String[C];
        st=new StringTokenizer(br.readLine());
        for(int i=0;i<C;i++){
            arr[i]=st.nextToken();
        }
        Arrays.parallelSort(arr);

        makePassword(L, arr, "", 0);

    }

    static boolean check(String password){
        int ja=0;
        int mo=0;
        for(char c:password.toCharArray()){
            if(c=='a'||c=='e'||c=='i'||c=='o'||c=='u'){
                mo++;
            }else{
                ja++;
            }
        }
        return ja>=2&&mo>=1;
    }

    static void makePassword(int L, String[] arr, String password, int idx){

        if(password.length()==L){
            if(check(password)) System.out.println(password);
            return;
        }

        if(idx>=arr.length){
            return;
        }

        makePassword(L, arr, password+arr[idx], idx+1); // idx위치 알파벳 사용한 경우
        makePassword(L, arr, password, idx+1); // idx위치 알파벳 사용할 수 있는데 사용하지 않은 경우
    }
}
