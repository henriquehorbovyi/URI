package beginner;

import java.util.Scanner;

public class Solution1019{
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int segInicial = s.nextInt();  
        int segTotal = segInicial % 60;  
        int minutos = segInicial / 60;  
        int minuto = minutos % 60;  
        int hora = minutos / 60;
        System.out.println(hora+":"+minuto+":"+segTotal);
     }
}
