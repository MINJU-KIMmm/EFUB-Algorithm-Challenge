import java.io.*;

class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        // 조카가 발음할 수 있는 단어의 개수
        // aya, ye, woo, ma 네 가지 발음 최대 1번씩 사용해 이어붙인 발음
        String[] words = {"aya", "ye", "woo", "ma"};
        
        for (String babb : babbling){
            for (String word : words){
                babb = babb.replaceFirst(word, "");
            }
            System.out.println(babb);
            if (babb.isEmpty()){
                answer++;
            }
            // if (babb.replaceAll(" ", "").equals("")){
            //     answer++;
            // }
        }
        
        return answer;
    }
}
