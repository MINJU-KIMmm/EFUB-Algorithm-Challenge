package HackerRank.medium;

import java.math.BigInteger;
import java.util.*;
import java.io.*;
public class ExtraLongFactorials {
    static class Result{
        static BigInteger[] dp;
        public static void extraLongFactorials(int n) {
            // Write your code here
            dp=new BigInteger[n+1];
            dp[0]= BigInteger.valueOf(0);
            dp[1]= BigInteger.valueOf(1);

            for(int i=2;i<=n;i++){
                dp[i]=dp[i-1].multiply(BigInteger.valueOf(i));
            }

            System.out.println(dp[n]);
        }
    }

    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);

        int n=sc.nextInt();

        Result.extraLongFactorials(n);

    }
}
