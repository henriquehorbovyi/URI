package beginner;

import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Solution1017 {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("#.000");
        
        double DistanciaPercorrida = s.nextDouble();
        double GastoCombustivel = s.nextDouble();
        
        double aux = GastoCombustivel / 12;
        double ConsumoDoAutomovel = DistanciaPercorrida * aux ;
        
        System.out.println(df.format(ConsumoDoAutomovel));           
    }
}
