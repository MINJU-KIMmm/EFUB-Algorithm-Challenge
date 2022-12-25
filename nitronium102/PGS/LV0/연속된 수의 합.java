class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        // x, x+1, x+2, x+3 = total
        // num*x + (for 0 ~ num-1) = total
        // x = (total - (0 ~ num-1) ) / num
        
        int sum = 0;
        for (int i=1; i<num; i++){
            sum += i;
        }
        int start = (total - sum) / num;
        
        for (int i=0; i<num; i++){
            answer[i] = start+i;
        }
            
        return answer;
    }
}
