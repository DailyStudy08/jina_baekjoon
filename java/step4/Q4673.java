/**
 * Q4673
 */
public class Q4673 {

    public static void main(String[] args) {
        
		int index = 10000; 
		boolean[] Number = new boolean[index]; //false 기본값
		
		for(int i=0; i< Number.length; i++) {
			if(d(i+1) < index+1)
				Number[d(i+1)-1] = true;
		}
		for(int i=0; i<Number.length; i++) {
			if(Number[i] == false)
				System.out.println(i+1);
		}
	}
	
	static int d(int n) {
		
		int sum = n;
		while(n > 0) { 
			sum += (n % 10); 
			n /= 10; 
		}
		
		return sum;
    }
}