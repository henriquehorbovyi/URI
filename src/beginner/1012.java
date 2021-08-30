import java.util.Locale;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        s.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("0.000");
          
        double PI = 3.14159;
        float A = s.nextFloat();
        float B = s.nextFloat();
        float C = s.nextFloat();
          
        float AreaTriangulo = A*C/2;
        double AreaCirculo = C*C*PI;
        double AreaTrapezio = ((A+B)*C)/2;
        double AreaQuadrado = B*B;
        double AreaRetalnulo = A*B;
          
        System.out.println("TRIANGULO: "+df.format(AreaTriangulo));
        System.out.println("CIRCULO: "+df.format(AreaCirculo));
        System.out.println("TRAPEZIO: "+df.format(AreaTrapezio));
        System.out.println("QUADRADO: "+df.format(AreaQuadrado));     
        System.out.println("RETANGULO: "+df.format(AreaRetalnulo));       
    }
}