package step07;

import java.util.Scanner;

public class Q2292 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 1;
        while (n>1) {
            n-=(6*cnt);
            cnt +=1;
        }
        System.out.println(cnt);
    }
}
