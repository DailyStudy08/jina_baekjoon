package class1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Q2562_2 {

	public static void main(String[] args) throws  IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[9];
		int max=0;
		int num=0;
		for(int i=0;i<9;i++) {
			arr[i]=Integer.parseInt(br.readLine());
			if(max<arr[i])
				{max=arr[i];
				num=i+1;} //인덱스 번호는 0부터 시작함  
		}
		System.out.println(max);
		System.out.println(num);
		
	}

}
