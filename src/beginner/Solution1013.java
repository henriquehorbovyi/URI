package beginner;

import java.util.Scanner;
 
public class Solution1013 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        
        int maior = -99999;         
        int a = s.nextInt();
        int b = s.nextInt();
        int c = s.nextInt();

        if(a > maior){
          maior = a;
        }
        if(b > maior){
          maior = b;
        }
        if(c > maior){
          maior = c;
        }
        System.out.println(maior+" eh o maior");    
    }
}
