#include <iostream>
#define N 10001 
using namespace std; 
int Calculate(int n){    
	int sum = n;    
	while (n > 0) {        
		sum += n % 10;        
		n /= 10;    
	}    return sum;} 
int main(){   
	bool selfNum[N] = {};  
	for (int i = 1; i < N; i++) {      
		int idx = Calculate(i);        
		if (idx <= N) selfNum[idx] = true;    
	}    
	for (int i = 1; i < N; i++) {        
		if (!selfNum[i]) 
			cout << i << endl;    
	}
	return 0;
}
