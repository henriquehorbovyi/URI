import java.text.DecimalFormat;
import java.util.Locale;
import java.util.Scanner;
 
public class Main {
    
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        s.useLocale(Locale.US);
        Locale.setDefault(Locale.US);
        DecimalFormat df = new DecimalFormat("0.00");
          
        int a,b,c,d,e,f , g,h,i,j,k,l;
        double N = s.nextDouble();
        
        System.out.println("NOTAS:");
        a=(int) (N/100);
        System.out.println(a+" nota(s) de R$ 100.00");
        b=(int) ((N-a*100)/50);
        System.out.println(b+" nota(s) de R$ 50.00");
        c=(int) ((N-a*100-b*50)/20);
        System.out.println(c+" nota(s) de R$ 20.00");
        d=(int) ((N-a*100-b*50-c*20)/10);
        System.out.println(d+" nota(s) de R$ 10.00");
        e=(int) ((N-a*100-b*50-c*20-d*10)/5);
        System.out.println(e+" nota(s) de R$ 5.00");
        f=(int) ((N-a*100-b*50-c*20-d*10-e*5)/2);
        System.out.println(f+" nota(s) de R$ 2.00");
        System.out.println("MOEDAS:");
        g=(int)(double)(N-a*100-b*50-c*20-d*10-e*5-f*2);
        System.out.println(g+" moeda(s) de R$ 1.00");
        h=(int)(double) ((N-a*100-b*50-c*20-d*10-e*5-f*2-g*1)/0.5); 
        System.out.println(h+" moeda(s) de R$ 0.50");
        i=(int)(double)((N-a*100-b*50-c*20-d*10-e*5-f*2-g*1-h*0.5)/0.25);
        System.out.println(i+" moeda(s) de R$ 0.25");
        j=(int)(double)((N-a*100-b*50-c*20-d*10-e*5-f*2-g*1-h*0.5-i*0.25)/0.1);
        System.out.println(j+" moeda(s) de R$ 0.10");
        k=(int)(double)((N-a*100-b*50-c*20-d*10-e*5-f*2-g*1-h*0.5-i*0.25-j*0.1)/0.05);
        System.out.println(k+" moeda(s) de R$ 0.05");
        l=(int)(double)((N-a*100-b*50-c*20-d*10-e*5-f*2-g*1-h*0.5-i*0.25-j*0.1-k*0.05)/0.01);
        System.out.println(l+" moeda(s) de R$ 0.01");
    }
}