package class1;

import java.util.Scanner;

public class Q2884 {
//"45분 일찍 알람 설정하기"
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int h = sc.nextInt();	
		int m = sc.nextInt();
		sc.close();
		if (m >= 45) {
			m -= 45;
		} else if (m < 45) {
			m = 60 - (45 - m);
			h -= 1;
		}
		if (h<0)
			h=23;
		System.out.print(h + " " + m);
	}
}
