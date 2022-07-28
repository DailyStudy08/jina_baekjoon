package class1;

import java.util.Scanner;

public class Q2908 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n1=sc.nextInt();
		int n2=sc.nextInt();
		n1=(n1/100)+(n1%10)*100+((n1/10)%10)*10;
		n2=(n2/100)+(n2%10)*100+((n2/10)%10)*10;
		if(n1>n2) {
			System.out.println(n1);
		}
		else
			System.out.println();
	}

}
