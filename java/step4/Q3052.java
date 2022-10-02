import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Q3052 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<Integer> lst = new ArrayList<>();
        for (int i = 0; i < 10; i++) {
            int n = sc.nextInt();
            if (!lst.contains(n%42)) {
                lst.add(n%42);
            }
        }
        System.out.println(lst.size());
        sc.close();
    }
}
