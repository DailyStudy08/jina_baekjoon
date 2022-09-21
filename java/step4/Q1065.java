import java.util.Scanner;

public class Q1065 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt=0;
        for (int i = 1; i < n+1; i++) {
            if (i<100) {
                cnt+=1;
            }
            else{
                if ((i/100)-((i%100)/10)==((i%100)/10)-(i%10)) {
                    cnt+=1;
                }
            }
        }
        System.out.println(cnt);
    }
}
