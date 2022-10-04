package step07;

import java.util.Scanner;

public class Q1193 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x =sc.nextInt();
        int n = 1;
        int a;
        int b;
        while (x>n) {
            x-=n;
            n++;
        }
        if (n%2==0) {
            a=x;
            b=n-x+1;
        }
        else{
            a=n-x+1;
            b=x;
        }
        System.out.println(a+"/"+b);
    }
}
