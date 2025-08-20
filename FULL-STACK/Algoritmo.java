public class Algoritmo {

    public static void main(String[] args) {
        dia_dia();
    }
    
    static boolean estouAtrasado() {
        return false;
    }
    
    static boolean AtrasadoOuCedo() {
        return true;
    }

    static void dia_dia() {
        System.out.println("Acordar");
        System.out.println("Desligar alarme");
        System.out.println("Levantar");
        System.out.println("Trocar de roupa");
        System.out.println("Ir ao banheiro");
        System.out.println("Ir para cozinha");
        System.out.println("Tomar cafe");
        System.out.println("Pegar mochila");
        System.out.println("Sair de casa");
        System.out.println("Pegar metro");

        if (estouAtrasado()) {
            System.out.println("Pegar onibus");
        } else {
            System.out.println("Pegar fretado");
        }

        System.out.println("Chegar na empresa");
        System.out.println("Estudar");
        System.out.println("Almocar");
        System.out.println("Estudar");
        System.out.println("Ir embora");

        if (AtrasadoOuCedo()) {
            System.out.println("Pegar onibus");
        } else {
            System.out.println("Pegar fretado");
        }
   }
}