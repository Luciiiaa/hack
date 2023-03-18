package idk;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Objects;
import java.util.Scanner;

public class obesenec{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String hadane = "";

        System.out.println("zadaj slovo");
        String slovo = scanner.nextLine();

        for (int i = 0; i < 30; i++) {
            System.out.println("");
        }

        String[] hovadina =slovo.split("");
        ArrayList<String> slovo2 = new ArrayList<String>(Arrays.asList(hovadina));

        int dlzka = slovo.length();

        for (int i = 0; i < dlzka; i++) {
            System.out.print("_");
            hadane += "_";
        }

        System.out.println("");

        String[] hovadina2 = hadane.split("");
        ArrayList<String> hadane2 = new ArrayList<String>(Arrays.asList(hovadina2));

        int p = 0;
        int zivoty = 0;

        while (!Objects.equals(slovo2, hadane2)) {
            System.out.println("Zadaj písmeno");
            String pismeno = scanner.nextLine();

            int o = 0;
            for (int i = 0; i < dlzka; i++) {
                if (Objects.equals(pismeno, slovo2.get(i))) {
                    hadane2.set(i, pismeno);
                    p = p +1;
                }

                else{
                    o = o +1;
                }

            }

            String slovooo = "";

            if(p > 0){
                p = 0;
                int zivot = 10 - zivoty;
                System.out.println("");

                for (int j = 0; j < dlzka; j++) {
                    slovooo += hadane2.get(j);
                }
                System.out.println(slovooo);

                if(slovooo.equals(slovo)){
                    System.out.println("VYHRAL SI! :)");
                    break;
                }

                System.out.println("Uhadol si! Ostava ti: " + zivot + " zivotov");
            }

            if(o == dlzka){
                o = 0;
                zivoty = zivoty + 1;
                int zivot = 10 - zivoty;

                for (int j = 0; j < dlzka; j++) {
                    slovooo += hadane2.get(j);
                }
                System.out.println(slovooo);

                if (zivoty == 10){
                    System.out.println("PREHRAL SI :( |" + " slovo bolo: " + slovo);
                    break;
                }
                System.out.println("Neuhadol si! Ostava ti: " + zivot + " zivotov");
            }

        }
    }
}