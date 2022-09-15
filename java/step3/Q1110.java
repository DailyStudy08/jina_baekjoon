import java.util.Scanner;

public class Q1110 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int r = sc.nextInt();
        int n = r;
        int cnt=0;
        while (true){
            if (n<10) {
                n=Integer.parseInt(""+n+n);
            }
            else{
                n= Integer.parseInt(""+(n%10) + ((n/10) + (n%10))%10);
            }
            cnt++;
            if (n==r) {
                break;
            }
        }
        System.out.println(cnt);
    }
}
