package BOJ;

import java.util.*;
import java.io.*;
public class No1389_케빈베이컨의6단계법칙 {

    static int[][] friend;
    static final int INF=(int)1e9; //무한대(경로 미지정)
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int N=Integer.parseInt(st.nextToken()); //사람 수
        int M=Integer.parseInt(st.nextToken()); //친구 관계 수

        //배열 초기화
        friend=new int[N+1][N+1];
        for(int i=1;i<N+1;i++){
            Arrays.fill(friend[i], INF);
        }

        //자기자신에게 가는 비용은 0으로 초기화
        for(int i=1;i<=N;i++){
            friend[i][i]=0;
        }

        //친구 정보 받아서 양방향으로 연결
        for(int i=0;i<M;i++){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            int b=Integer.parseInt(st.nextToken());

            friend[a][b]=1;
            friend[b][a]=1;
        }

        //플로이드워셜 계산
        for(int i=1;i<=N;i++){
            for(int a=1;a<=N;a++){
                for(int b=1;b<=N;b++){
                    friend[a][b]=Math.min(friend[a][b], friend[a][i]+friend[i][b]);
                }
            }
        }

        //정답 계산 위한 배열
        Person[] answer=new Person[N+1];
        answer[0]=new Person(0, INF);
        //합 계산(케빈베이컨 값)
        //모든 친구들이 연결되어 있기 때문에 계산 완료 후에는 INF인 값 없음
        for(int i=1;i<=N;i++){
            int sum=0;
            for(int j=1;j<=N;j++){
                sum+=friend[i][j];
            }

            answer[i]=new Person(i,sum);
        }

        //sum 기준으로 정렬, sum이 같을 때는 idx 기준
        Arrays.sort(answer);

        //정답 출력
        System.out.println(answer[0].idx);
    }
}

//정답 배열에 쓸 Person 배열
//sum->idx 기준으로 정렬되게 만들어 준다.
class Person implements Comparable<Person>{
    int idx, sum;

    public Person(int idx, int sum){
        this.idx=idx;
        this.sum=sum;
    }

    public int compareTo(Person o){
        if(this.sum==o.sum) return Integer.compare(this.idx, o.idx);
        return Integer.compare(this.sum, o.sum);
    }
}