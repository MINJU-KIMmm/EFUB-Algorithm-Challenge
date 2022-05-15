package BOJ.graph;

import java.util.*;
import java.io.*;
public class No11404_플로이드{
    static final int INF=(int)1e9;
    static int[][] arr;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int m=Integer.parseInt(br.readLine());

        arr=new int[n+1][n+1];

        for(int i=0;i<=n;i++){
            Arrays.fill(arr[i],INF);
        }

        for(int i=1;i<=n;i++){
            arr[i][i]=0;
        }

        for(int t=0;t<m;t++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            //입력된 비용 중 최소 비용을 저장
            if(arr[a][b]>c) arr[a][b]=c;
        }

        for(int k=1;k<=n;k++){
            for(int i=1;i<=n;i++){
                for(int j=1;j<=n;j++){
                    arr[i][j]=Math.min(arr[i][j], arr[i][k]+arr[k][j]);
                }
            }
        }

        for(int i=1;i<=n;i++){
            for(int j=1;j<=n;j++){
                if(arr[i][j]==INF) System.out.print(0+" ");
                else{
                    System.out.print(arr[i][j]+" ");
                }
            }
            System.out.println();
        }

    }
}
