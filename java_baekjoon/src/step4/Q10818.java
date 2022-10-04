package step4;

import java.util.Scanner;

public class Q10818 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < arr.length; i++) {
            int m = sc.nextInt();
            arr[i]=m;
        }
        int max=arr[0];
        int min= arr[0];
        for (int i = 0; i < arr.length; i++) {
            if (arr[i]>max) {
                max=arr[i];
            }
            if (arr[i]<min) {
                min=arr[i];
            }
        }
        System.out.println(min+" "+max);
        sc.close();

    }
}
