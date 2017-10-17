import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("#.0000");
        double PI = 3.14159;
        double raio;
        double area;
        raio = s.nextDouble();
        area = Math.pow(raio, 2)* PI;       
        System.out.println("A="+df.format(area));
    }
     
}