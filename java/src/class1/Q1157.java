package class1;

import java.util.Scanner;

public class Q1157 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine().toUpperCase();
		sc.close();
		int[] count = new int[26];
		for (int i = 0; i < str.length(); i++) {
			int n = str.charAt(i) - 'A';
			count[n]++;
		}
		int max = 0;
		char m = '?';
		for (int i = 0; i < count.length; i++) {
			if (max < count[i]) {
				max = count[i];
				m = (char) ('A' + i);
			} else if (max == count[i]) {
				m = '?';
			}
		}
		System.out.println(m);

	}

}
