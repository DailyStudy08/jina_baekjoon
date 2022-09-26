import java.util.Scanner;

public class Q2941 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String[] str = {"c=","c-","dz=","d-","lj","nj","s=","z="};
        String s = sc.next();
        for (int i = 0; i < str.length; i++) {
            if(s.contains(str[i])){
                s=s.replaceAll(str[i], "a");
            }
        }
        System.out.println(s.length());
        sc.close();
    }
}
