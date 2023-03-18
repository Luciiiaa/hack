package idk;

import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class loteria2 {
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";

    public static void main(String[] args) {
        Random random = new Random();
        Scanner scanner = new Scanner(System.in);

        ArrayList<Integer> cisla_hrac = new ArrayList<Integer>();
        ArrayList<Integer> cisla_nahodne = new ArrayList<Integer>();

        System.out.println(ANSI_CYAN + "Vitajte v lotérii!" + ANSI_RESET);
        System.out.println(ANSI_CYAN + "Zadajte prosím 5 čísel v rozmedzí od 1 do 80." + ANSI_RESET);
        System.out.println("");

        int i = 0;
        while(i < 5) {
            int n_cislo = random.nextInt(1, 80);

            if(!cisla_nahodne.contains(n_cislo)){
                i = i + 1;
                cisla_nahodne.add(n_cislo);
            }
        }

        int a = 0;
        int f = 1;
        while (a != 5) {
            System.out.println(ANSI_YELLOW + "Zadajte " + f + ". číslo!" + ANSI_RESET);
            int zadane = scanner.nextInt();

            if (zadane >= 1 && zadane < 80){
                if (!cisla_hrac.contains(zadane)){
                    a = a + 1;
                    f = f + 1;
                    cisla_hrac.add(zadane);
                }

                else{
                    System.out.println(ANSI_RED + "Číslo ste už zadali! Zadajte číslo ešte raz prosím." + ANSI_RESET);
                    System.out.println("");
                }
            }

            else{
                System.out.println(ANSI_RED + "Zadali ste nesprávnu hodnotu! Zadajte číslo ešte raz prosím." + ANSI_RESET);
                System.out.println("");
            }
        }

        int pocitadlo = 0;
        for (int j = 0; j < cisla_nahodne.size(); j++) {
            int porovnanie = cisla_hrac.get(j);

            if(cisla_nahodne.contains(porovnanie)){
                pocitadlo = pocitadlo + 1;
            }
        }

        System.out.println(ANSI_CYAN + "Vaše zadané čísla: " + ANSI_RESET + cisla_hrac );
        System.out.println(ANSI_CYAN + "Vylosované čísla: " +  ANSI_RESET + cisla_nahodne );
        System.out.println(ANSI_YELLOW + "Váš celkový počet uhádnutých čísel: " + pocitadlo + ANSI_RESET);

        if(pocitadlo>0){
            System.out.println(ANSI_GREEN + "Gratulujeme!" + ANSI_RESET );
        }
    }
}