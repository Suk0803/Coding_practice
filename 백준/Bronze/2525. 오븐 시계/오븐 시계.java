import java.util.*;

public class  Main {
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);

        int a = input.nextInt();
        int b = input.nextInt();
        int c = input.nextInt();

        b += c;
        int d = b / 60;
        if ( d >= 1){
            a += d;
            b = b % 60;
            if ( a >= 24) {
                a -= 24;
            }
            
        }
        System.out.printf("%d %d", a, b);

    }
}
