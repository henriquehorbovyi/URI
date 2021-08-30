import java.util.Scanner;
 
public class Main {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int idade = s.nextInt();
        int a =  idade/365;
        int m = (idade%365)/30;
        int d = (idade%365)%30;
        System.out.println(a+" ano(s)");
        System.out.println(m+" mes(es)");
        System.out.println(d+" dia(s)");
    }
}