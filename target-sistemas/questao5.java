import java.util.Scanner;

public class InverterString {

    public static void main(String[] args) {
        // Criação do objeto Scanner para leitura da entrada do usuário
        Scanner scanner = new Scanner(System.in);
        
        // Solicita a entrada da string do usuário
        System.out.println("Digite uma string para inverter:");
        String input = scanner.nextLine();
        
        // Fecha o scanner
        scanner.close();
        
        // Inverte a string
        String reversedString = inverterString(input);
        
        // Imprime o resultado
        System.out.println("String invertida: " + reversedString);
    }

    // Método para inverter a string
    public static String inverterString(String str) {
        char[] caracteres = str.toCharArray(); // Converte a string para um array de caracteres
        int esquerda = 0;
        int direita = caracteres.length - 1;

        // Troca os caracteres do início e do fim até encontrar o meio
        while (esquerda < direita) {
            // Troca os caracteres
            char temp = caracteres[esquerda];
            caracteres[esquerda] = caracteres[direita];
            caracteres[direita] = temp;

            // Move os ponteiros
            esquerda++;
            direita--;
        }

        // Converte o array de caracteres de volta para uma string e retorna
        return new String(caracteres);
    }
}
