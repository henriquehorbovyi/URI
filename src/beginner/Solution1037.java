package beginner;

import java.util.Locale;
import java.util.Scanner;

public class Solution1037 {

   public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
      s.useLocale(Locale.US);
       
      float N = s.nextFloat();
     
      if(N < 0 || N > 100.01)System.out.println("Fora de intervalo"); 
      if(N >= 0 && N <= 25)System.out.println("Intervalo [0,25]");
      if(N >= 25.01 && N <= 50)System.out.println("Intervalo (25,50]");
      if(N >= 50.01 && N <= 75)System.out.println("Intervalo (50,75]");
      if(N >= 75.01 && N <= 100)System.out.println("Intervalo (75,100]");
   }
}
