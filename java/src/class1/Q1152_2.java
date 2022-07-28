package class1;

import java.util.Scanner;
import java.util.StringTokenizer;
 
public class Q1152_2 {
 
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
 
		String Str = sc.nextLine();
		sc.close();
 
		StringTokenizer st = new StringTokenizer(Str," ");
		
		System.out.println(st.countTokens());	
		
	}
 
}