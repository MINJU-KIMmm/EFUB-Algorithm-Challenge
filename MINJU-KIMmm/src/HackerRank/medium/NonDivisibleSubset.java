package HackerRank.medium;

import java.util.*;
import java.io.*;

public class NonDivisibleSubset {
    public static int nonDivisibleSubset(int k, List<Integer> s) {
        // Write your code here
        int[] cnt=new int[k];
        for(int num:s){
            cnt[num%k]++;
        }

        int answer=0;
        if(cnt[0]>0) answer++;
        if(k%2==0&&cnt[k/2]>0) answer++;
        for(int i=1;i<=(k-1)/2;i++){
            answer+=cnt[i]>cnt[k-i]? cnt[i]:cnt[k-i];
        }

        return answer;
    }

}
