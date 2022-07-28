package class1;
//단어의 개수 
import java.util.Scanner;

public class Q1152 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str=sc.nextLine(); 
		sc.close();
		str = str.trim();
		if(str.isBlank()) System.out.println(0);
		else {
		String arr[] = str.split(" ");
		System.out.println(arr.length);}
	}

}
