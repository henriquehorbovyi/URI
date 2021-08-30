import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        s.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("#.000");
        int R = s.nextInt();
        double PI = 3.14159;
        double aux = 4/3;
        double volume = (4/3.0) * PI *Math.pow(R,3);
        System.out.println("VOLUME = "+df.format(volume)); 
    }
}