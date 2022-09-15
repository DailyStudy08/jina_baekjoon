import java.util.Scanner;

public class Q25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total=sc.nextInt();
        int n = sc.nextInt();
        int check=0;
        for(int i=0;i<n;i++){
            int price=sc.nextInt();
            int m = sc.nextInt();
            check+=(price*m);
        }
        if (check==total){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
    }
}
