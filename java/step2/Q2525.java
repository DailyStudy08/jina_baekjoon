import java.util.Scanner;

public class Q2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int h = sc.nextInt();
        int m = sc.nextInt();
        int plus = sc.nextInt();
        h=h+(plus/60);
        m=m+(plus%60);
        if (m>=60){
            h++;
            m-=60;
        }
        if (h>=24){
            h-=24;
        }
        System.out.println(h+" "+m);
    }
}
