package beginner;

import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Solution1006 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        s.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df =  new DecimalFormat("#.0");
        double A = s.nextDouble();
        double B = s.nextDouble();
        double C = s.nextDouble();
        double media = (A*2 + B*3 + C*5) / 10;
        System.out.println("MEDIA = "+df.format(media));
    }
}
