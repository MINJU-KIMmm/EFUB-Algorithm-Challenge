package HackerRank.easy;

import java.io.*;
import java.util.*;
public class AVeryBigSum {

    public static void main(String[] args) throws IOException{

    }
}

class Result {

    /*
     * Complete the 'aVeryBigSum' function below.
     *
     * The function is expected to return a LONG_INTEGER.
     * The function accepts LONG_INTEGER_ARRAY ar as parameter.
     */

    public static long aVeryBigSum(List<Long> ar) {
        // Write your code here
        long sum=0;
        for(long num:ar){
            sum+=num;
        }

        return sum;
    }

}
