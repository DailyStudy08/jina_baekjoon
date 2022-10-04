package step4;

import java.util.Scanner;

public class Q8958 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n =sc.nextInt();
        String arr[] = new String[n];

        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.next();
        }
        sc.close();

        for (int i = 0; i < arr.length; i++) {

            int cnt = 0;
            int result = 0;

            for (int j = 0; j < arr[i].length(); j++) {
                if (arr[i].charAt(j) == 'O') {
                    cnt++;
                }
                else {
                    cnt = 0;
                }
                result += cnt;
            }
            System.out.println(result);
        }
    }
}
