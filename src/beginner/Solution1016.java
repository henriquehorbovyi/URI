package beginner;
import java.util.Scanner;

public class Solution1016{
  	public static void main(String[] args) {
    	Scanner s = new Scanner(System.in);
	  	int Dif = 90 - 60;
	  	int distancia = s.nextInt();
	  	int mimtotal = distancia * 60;
	  	int total = mimtotal/Dif;
	  	System.out.println(total+" minutos");
  	}
}
