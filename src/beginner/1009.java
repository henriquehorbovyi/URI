import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Main {
  
    public static void main(String[] args) {
         
        Scanner s  = new Scanner(System.in);
        s.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("#.00");
         
        String nome = s.next();
        double SalarioFixo = s.nextDouble();
        double valorVendasEfetuadas = s.nextDouble();
         
        double ValorPorcentagem = valorVendasEfetuadas * 0.15;
        double Total = ValorPorcentagem + SalarioFixo;
         
        System.out.println("TOTAL = "+"R$ "+df.format(Total));
         
    }
}