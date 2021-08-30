package beginner;

import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Solution1008 {
 
    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        s1.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("#.00");         
        int numero = s1.nextInt();
        int horasTrabalho = s1.nextInt();
        double ValorPorHora = s1.nextDouble();
        double Salario = horasTrabalho * ValorPorHora ;
        System.out.println("NUMBER = "+numero);
        System.out.println("SALARY = " +"U$ "+df.format(Salario));         
         
    }
}
