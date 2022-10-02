import java.util.Scanner;

public class Q1316 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int cnt=n;
        for (int i = 0; i < n; i++) {
            int[] v = new int[26];
            String str=sc.next();
            boolean flag=true;
            for (int j = 0; j < str.length(); j++) {
                if (flag==false) break;
                int m=str.charAt(j)-97;
                if (j==0 || v[m]==0) { //처음나온다면
                    v[m]+=1;
                }
                else{ //처음나오는게 아니라면
                    if(str.charAt(j)!=str.charAt(j-1)){ //전과 다르면
                        cnt--;
                        flag=false;
                        continue;
                    } //한번 false이면 끝
                }
            }
        }
        System.out.println(cnt);
    }
}
