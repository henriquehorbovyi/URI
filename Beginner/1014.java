import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;

public class Main {
   public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
      s.useLocale(Locale.US);
      Locale.setDefault(Locale.US);
      DecimalFormat df = new DecimalFormat("#.000");
        
      int DistanciaPercorrida = s.nextInt();
      double GastoCombustivel = s.nextDouble();
      double ConsumoDoAutomovel = DistanciaPercorrida / GastoCombustivel;
      System.out.println(df.format(ConsumoDoAutomovel)+" km/l"); 
   }
}