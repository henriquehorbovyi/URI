package beginner;

import java.text.DecimalFormat;
import java.util.Scanner;
 
public class Solution1018 {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.00");
            
        int N,a,b,c,d,e,f,g;
        N = s.nextInt();
          
        System.out.println(N);
        a = N/100;
        System.out.println(a+" nota(s) de R$ 100,00");
        b=(N-a*100)/50;
        System.out.println(b+" nota(s) de R$ 50,00");
        c=(N-a*100-b*50)/20;
        System.out.println(c+" nota(s) de R$ 20,00");
        d=(N-a*100-b*50-c*20)/10;
        System.out.println(d+" nota(s) de R$ 10,00");
        e=(N-a*100-b*50-c*20-d*10)/5;
        System.out.println(e+" nota(s) de R$ 5,00");
        f=(N-a*100-b*50-c*20-d*10-e*5)/2;
        System.out.println(f+" nota(s) de R$ 2,00");
        g=(N-a*100-b*50-c*20-d*10-e*5-f*2);
        System.out.println(g+" nota(s) de R$ 1,00");
    }
}
