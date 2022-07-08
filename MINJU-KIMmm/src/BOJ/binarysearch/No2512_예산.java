package BOJ.binarysearch;

import java.io.*;
import java.util.*;
public class No2512_예산 {
    static int[] arr;
    public static void main(String[] args) throws IOException {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

        int N=Integer.parseInt(br.readLine());
        arr=new int[N];
        StringTokenizer st=new StringTokenizer(br.readLine());
        int sum=0;
        for(int i=0;i<N;i++){
            arr[i]=Integer.parseInt(st.nextToken());
            sum+=arr[i];
        }

        int M=Integer.parseInt(br.readLine());

        Arrays.sort(arr); //정렬
        int left=0; //상한선으로 가능한 수 중 최소
        int right=arr[arr.length-1]; //예산으로 가능한 수 중 최대(최대로 요구하는 돈을 넘어서는 상한선은 필요 없음)

        int answer=0;


        while(left<=right){ //<로 하면 틀림
            int mid=(left+right)/2;

            int give=0;
            for(int num:arr){
                give+=Math.min(mid, num);
            }

            //예산보다 주는 돈이 더 적거나 같은 경우 -> 더 넉넉하게 잡아도 된다는 뜻
            if(give<=M){
                answer=mid; //answer=Math.max(answer, mid)
                left=mid+1;
            }
            //예산보다 주는 돈이 더 큰 경우 -> 예산 총액 초과, 더 타이트하게 잡아야 한다는 뜻
            else{
                right=mid-1;
            }
        }

        System.out.println(answer);
    }
}
